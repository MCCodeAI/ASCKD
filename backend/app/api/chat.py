from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict, Any, Union
import os
from dotenv import load_dotenv
from fastapi.responses import StreamingResponse
import json
import asyncio
from pydantic_ai.agent import Agent, RunContext
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
import logging
import httpx
from dataclasses import dataclass
import weaviate
from utils.structured_docs_wv import WVStructuredDocsManager

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logging.getLogger("primp").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Configuration
LOG_RAG_RESULTS = True

router = APIRouter()

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    stream: bool = False
    model: str = "gpt-4o-mini"

# ============================================================================
# PYDANTIC AI MODEL SETUP
# ============================================================================

def create_model_instance(model: str = "gpt-4o-mini") -> Union[str, OpenAIChatModel]:
    """
    Create OpenAI model instance for Pydantic AI.
    """
    # Get API configuration from environment
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL")
    
    # Create OpenAI provider with configuration
    if base_url:
        provider = OpenAIProvider(
            api_key=api_key,
            base_url=base_url
        )
    else:
        provider = OpenAIProvider(api_key=api_key)
    
    # Create and return OpenAIChatModel
    return OpenAIChatModel(
        model_name=model,
        provider=provider
    )

# ============================================================================
# RAG TOOL (Weaviate Vector Search)
# ============================================================================

# Global cache for Weaviate manager (lazy initialization)
_wv_manager_cache = None

def get_weaviate_manager() -> WVStructuredDocsManager:
    """
    Get or create Weaviate manager instance (singleton pattern).
    Only initializes connection when actually needed.
    """
    global _wv_manager_cache
    
    if _wv_manager_cache is None:
        logger.info("Initializing Weaviate manager (first RAG call)")
        voyageai_key = os.getenv("VOYAGEAI_APIKEY")
        _wv_manager_cache = WVStructuredDocsManager(
            url="http://localhost:8090",
            voyageai_key=voyageai_key
        )
    
    return _wv_manager_cache

@dataclass
class RAGDeps:
    pass  # No longer needs to hold the manager

async def rag_search_tool(ctx: RunContext[RAGDeps], query: str) -> str:
    """
    Search for relevant documentation using Weaviate hybrid search.
    
    Hybrid search combines:
    - Vector search (semantic similarity)
    - Keyword search (BM25)
    
    Args:
        ctx: The run context
        query: The search query
        
    Returns:
        Retrieved documentation as a string with clickable URLs
    """
    logger.info(f"RAG hybrid search requested for: {query}")
    
    try:
        # Get Weaviate manager (lazy initialization on first call)
        wv_manager = get_weaviate_manager()
        
        # Search sdbody collection using hybrid search
        collection = wv_manager.client.collections.get("sdbody")
        
        # Perform hybrid search (vector + keyword) for better results
        # alpha=0.75 means 75% vector search, 25% keyword search
        # This balances semantic understanding with exact keyword matching
        from weaviate.classes.query import MetadataQuery
        
        results = collection.query.hybrid(
            query=query,
            limit=5,  # k=5 as requested
            alpha=0.75,  # Balance: 0.0=pure keyword, 0.5=balanced, 1.0=pure vector
            return_metadata=MetadataQuery(score=True)
        )
        
        if not results.objects:
            return f"No relevant documentation found for '{query}'."
        
        # Format results with clickable URLs
        formatted_results = f"Retrieved documentation for '{query}':\n\n"
        for i, obj in enumerate(results.objects, 1):
            props = obj.properties
            name = props.get("name", "Unknown")
            content = props.get("content", "")
            doc_type = props.get("type", "Unknown")
            path = props.get("path", "Unknown")
            
            # Convert file path to accessible URL
            # Path format could be:
            # - backend/structured_docs/wmxmanual/file.html
            # - structured_docs/wmxmanual/file.html  
            # - wmxmanual/file.html
            # Convert to: http://localhost:5173/docs/wmxmanual/file.html
            
            # Debug: log the original path
            logger.info(f"Original path from Weaviate: {path}")
            
            doc_url = path
            if "structured_docs/" in path:
                # Extract the path after structured_docs/
                relative_path = path.split("structured_docs/", 1)[1]
                doc_url = f"http://localhost:5173/docs/{relative_path}"
            elif path.startswith("wmxmanual/") or "/" in path:
                # Path is already relative (e.g., wmxmanual/file.html)
                doc_url = f"http://localhost:5173/docs/{path}"
            else:
                # Fallback: assume it's just a filename
                doc_url = f"http://localhost:5173/docs/{path}"
            
            logger.info(f"Generated URL: {doc_url}")
            
            # Get hybrid search score
            score_info = ""
            if hasattr(obj.metadata, 'score') and obj.metadata.score is not None:
                score_info = f" (score: {obj.metadata.score:.4f})"
            
            formatted_results += f"{i}. {name} ({doc_type}){score_info}\n"
            formatted_results += f"   Source: {doc_url}\n"
            formatted_results += f"   Content: {content}\n\n"
        
        logger.info(f"RAG hybrid search returned {len(results.objects)} results")
        
        if LOG_RAG_RESULTS:
            logger.info("=== RAG SEARCH RESULTS START ===")
            # Create a truncated version for logging
            log_output = f"Retrieved documentation for '{query}':\n\n"
            for i, obj in enumerate(results.objects, 1):
                props = obj.properties
                name = props.get("name", "Unknown")
                content = props.get("content", "")
                doc_type = props.get("type", "Unknown")
                path = props.get("path", "Unknown")
                
                # Truncate content for logging
                content_preview = content[:500] + "..." if len(content) > 500 else content
                
                # Reconstruct URL logic for logging (simplified)
                doc_url = path
                if "structured_docs/" in path:
                    relative_path = path.split("structured_docs/", 1)[1]
                    doc_url = f"http://localhost:5173/docs/{relative_path}"
                elif path.startswith("wmxmanual/") or "/" in path:
                    doc_url = f"http://localhost:5173/docs/{path}"
                else:
                    doc_url = f"http://localhost:5173/docs/{path}"
                
                # Get score
                score_info = ""
                if hasattr(obj.metadata, 'score') and obj.metadata.score is not None:
                    score_info = f" (score: {obj.metadata.score:.4f})"
                
                log_output += f"{i}. {name} ({doc_type}){score_info}\n"
                log_output += f"   Source: {doc_url}\n"
                log_output += f"   Content: {content_preview}\n\n"
                
            logger.info(log_output)
            logger.info("=== RAG SEARCH RESULTS END ===")
            
        return formatted_results
        
    except Exception as e:
        logger.error(f"RAG search failed: {e}")
        return f"Error searching documentation: {str(e)}"

# ============================================================================
# AGENT CREATION
# ============================================================================

# Global cache for agent instance
_cached_agent = None
_cached_model = None

def create_rag_agent(model: str = "gpt-4o-mini") -> Agent:
    """
    Create or reuse RAG agent with the specified model.
    """
    global _cached_agent, _cached_model
    
    # Reuse cached agent if model hasn't changed
    if _cached_agent is not None and _cached_model == model:
        return _cached_agent
    
    # Create model instance
    model_instance = create_model_instance(model)
    
    # Create agent with system prompt
    instructions = """You are a helpful AI assistant with access to a documentation database.
You have access to a 'rag_search_tool' that can search for relevant information from the documentation using semantic vector search.

DECISION PROCESS:
Analyze the user's request to determine if you need to search the documentation to answer accurately.
- If the user asks about specific documentation, technical details, procedures, or domain-specific knowledge that might be in the documentation -> USE the 'rag_search_tool'.
- If the user asks for general knowledge, coding help, casual conversation, or common questions you can answer directly -> Answer WITHOUT using the tool.

When using the tool:
1. Formulate a specific search query based on the user's question.
2. Call 'rag_search_tool' with that query.
3. The tool will return up to 5 most relevant documentation chunks.
4. Use the retrieved documentation to construct your answer.
5. Always cite the source documentations (file path) as links when referencing specific information.
6. If the retrieved documentation doesn't fully answer the question, acknowledge the limitations and provide what information is available.

Example:
User: "How do I configure the webhook?" -> Call rag_search_tool("webhook configuration")
User: "Write a python script" -> Answer directly
User: "What's the manual procedure for X?" -> Call rag_search_tool("procedure X")"""
    
    agent = Agent(
        model=model_instance,
        instructions=instructions,
        retries=2,
        deps_type=RAGDeps
    )
    
    # Add RAG search tool to the agent
    agent.tool(rag_search_tool)
    
    # Cache the agent
    _cached_agent = agent
    _cached_model = model
    
    return agent

# ============================================================================
# STREAMING RESPONSE HANDLER
# ============================================================================

async def generate_stream_pydantic(messages: List[Message], model: str):
    """
    Generate streaming response using Pydantic AI agent with RAG.
    """
    try:
        # Get or create agent
        agent = create_rag_agent(model)
        
        # Create dependencies (no need to initialize Weaviate here)
        # It will be lazily initialized when tool is actually called
        deps = RAGDeps()
        
        # Convert messages from Ant Design X format to Pydantic AI format
        from pydantic_ai.messages import ModelRequest, ModelResponse, UserPromptPart, TextPart
        
        message_history = []
        user_prompt = ""
        
        for msg in messages:
            if msg.role == "user":
                message_history.append(
                    ModelRequest(parts=[UserPromptPart(content=msg.content)])
                )
                user_prompt = msg.content
            elif msg.role == "assistant":
                message_history.append(
                    ModelResponse(parts=[TextPart(content=msg.content)])
                )
        
        # Remove the last user message from history since it will be the prompt
        if message_history and isinstance(message_history[-1], ModelRequest):
            message_history = message_history[:-1]
        
        # Log message history for debugging
        logger.debug(f"Message History: {message_history}")
        logger.info(f"User Prompt: {user_prompt}")
        
        # Create a unique ID for this completion
        completion_id = f"chatcmpl-{os.urandom(12).hex()}"
        created_timestamp = int(asyncio.get_event_loop().time())
        
        # Accumulate response for logging
        full_response = ""
        
        # Stream response from Pydantic AI agent with full message history and deps
        async with agent.run_stream(
            user_prompt,
            message_history=message_history if message_history else None,
            deps=deps
        ) as result:
            async for text_chunk in result.stream_text(delta=True):
                if text_chunk:
                    full_response += text_chunk  # Accumulate for logging
                    # Format as OpenAI streaming chunk
                    response_data = {
                        "id": completion_id,
                        "object": "chat.completion.chunk",
                        "created": created_timestamp,
                        "model": model,
                        "choices": [{
                            "index": 0,
                            "delta": {
                                "content": text_chunk
                            },
                            "finish_reason": None
                        }]
                    }
                    yield f"data: {json.dumps(response_data)}\n\n"
        
        # Log the response preview (first 200 chars)
        response_preview = full_response[:200] + "..." if len(full_response) > 200 else full_response
        logger.info(f"AI Response: {response_preview}")
        
        # Send final chunk with finish_reason
        final_chunk = {
            "id": completion_id,
            "object": "chat.completion.chunk",
            "created": created_timestamp,
            "model": model,
            "choices": [{
                "index": 0,
                "delta": {},
                "finish_reason": "stop"
            }]
        }
        yield f"data: {json.dumps(final_chunk)}\n\n"
        yield "data: [DONE]\n\n"
        
    except Exception as e:
        logger.error(f"Stream error: {str(e)}")
        error_data = {"error": {"message": str(e), "type": "server_error"}}
        yield f"data: {json.dumps(error_data)}\n\n"

# ============================================================================
# CHAT ENDPOINT
# ============================================================================

@router.post("/chat")
async def chat(request: ChatRequest):
    """
    Chat endpoint that uses Pydantic AI agent for responses.
    """
    if request.stream:
        return StreamingResponse(
            generate_stream_pydantic(request.messages, request.model),
            media_type="text/event-stream"
        )
    else:
        try:
            # Get or create agent
            agent = create_rag_agent(request.model)
            
            # Create dependencies (no need to initialize Weaviate here)
            # It will be lazily initialized when tool is actually called
            deps = RAGDeps()
            
            # Convert messages from Ant Design X format to Pydantic AI format
            from pydantic_ai.messages import ModelRequest, ModelResponse, UserPromptPart, TextPart
            
            message_history = []
            user_prompt = ""
            
            for msg in request.messages:
                if msg.role == "user":
                    message_history.append(
                        ModelRequest(parts=[UserPromptPart(content=msg.content)])
                    )
                    user_prompt = msg.content
                elif msg.role == "assistant":
                    message_history.append(
                        ModelResponse(parts=[TextPart(content=msg.content)])
                    )
            
            # Remove the last user message from history since it will be the prompt
            if message_history and isinstance(message_history[-1], ModelRequest):
                message_history = message_history[:-1]
            
            # Log message history for debugging
            logger.debug(f"Message History: {message_history}")
            logger.info(f"User Prompt: {user_prompt}")
            
            # Run agent with full message history and deps
            result = await agent.run(
                user_prompt,
                message_history=message_history if message_history else None,
                deps=deps
            )
            
            # Log the response preview (first 200 chars)
            # In this version of pydantic-ai, the result is in .output
            response_content = result.output
                
            response_preview = response_content[:200] + "..." if len(response_content) > 200 else response_content
            logger.info(f"AI Response: {response_preview}")
            
            # Format response to match expected structure
            response = {
                "id": f"chatcmpl-{os.urandom(12).hex()}",
                "content": response_content,
                "role": "assistant"
            }
            
            return response
            
        except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))

