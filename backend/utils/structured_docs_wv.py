import weaviate
from weaviate.classes.config import Property, DataType, ReferenceProperty, Configure
from typing import Dict, Any, List, Optional
import os
import re
import logging
import uuid
from .token_counter import count_tokens

# Setup logging
logger = logging.getLogger(__name__)

class WVStructuredDocsManager:
    """Manages structured documentation data operations in WV v4."""
    
    # Configuration for content chunking
    MAX_TOKENS_PER_CHUNK = 8000  # Token limit with safety buffer (OpenAI standard is 8192)
    
    def __init__(self, url: str = "http://localhost:8090", openai_key: str = None, voyageai_key: str = None, grpc_port: int = 50051, max_tokens: int = None):
        headers = {}
        if openai_key:
            headers["X-OpenAI-Api-Key"] = openai_key
        if voyageai_key:
            headers["X-VoyageAI-Api-Key"] = voyageai_key
        
        # Allow override of max tokens per chunk
        if max_tokens is not None:
            self.MAX_TOKENS_PER_CHUNK = max_tokens
            
        from urllib.parse import urlparse
        parsed = urlparse(url)
        host = parsed.hostname or "localhost"
        port = parsed.port or 8090
        
        if host in ["localhost", "127.0.0.1", "0.0.0.0"]:
            self.client = weaviate.connect_to_local(
                port=port,
                grpc_port=grpc_port,
                headers=headers
            )
        else:
            secure = parsed.scheme == "https"
            self.client = weaviate.connect_to_custom(
                http_host=host,
                http_port=port,
                http_secure=secure,
                grpc_host=host,
                grpc_port=grpc_port,
                grpc_secure=secure,
                headers=headers
            )
            
        logger.info(f"WVStructuredDocsManager initialized, connected to {url} (grpc: {grpc_port})")
        logger.info(f"Max tokens per chunk: {self.MAX_TOKENS_PER_CHUNK}")
        self.ensure_schema()

    def close(self):
        self.client.close()

    def ensure_schema(self):
        """Ensures the schema for sddir, sdfile, and sdbody exists."""
        try:
            from weaviate.classes.config import Tokenization
            
            # sddir
            if not self.client.collections.exists("sddir"):
                print("DEBUG: Creating sddir with vector config...")
                self.client.collections.create(
                    name="sddir",
                    vector_config=Configure.Vectors.text2vec_voyageai(model="voyage-3.5-lite"),
                    properties=[
                        Property(name="name", data_type=DataType.TEXT), # d1_dirname
                        Property(
                            name="path", 
                            data_type=DataType.TEXT,
                            tokenization=Tokenization.FIELD  # Don't tokenize - exact match only
                        ),
                        Property(name="level", data_type=DataType.INT),
                    ]
                )
                logger.info("Created collection: sddir")

            # sdfile
            if not self.client.collections.exists("sdfile"):
                print("DEBUG: Creating sdfile with vector config...")
                from weaviate.classes.config import Tokenization
                self.client.collections.create(
                    name="sdfile",
                    vector_config=Configure.Vectors.text2vec_voyageai(model="voyage-3.5-lite"),
                    properties=[
                        Property(name="name", data_type=DataType.TEXT), # f_filename
                        Property(
                            name="path", 
                            data_type=DataType.TEXT,
                            tokenization=Tokenization.FIELD  # Don't tokenize - exact match only
                        ),
                    ],
                    references=[
                        ReferenceProperty(name="indir", target_collection="sddir")
                    ]
                )
                logger.info("Created collection: sdfile")

            # sdbody
            if not self.client.collections.exists("sdbody"):
                print("DEBUG: Creating sdbody with vector config...")
                self.client.collections.create(
                    name="sdbody",
                    vector_config=Configure.Vectors.text2vec_voyageai(model="voyage-3.5-lite"),
                    properties=[
                        Property(name="name", data_type=DataType.TEXT), # body_s or h1_headername
                        Property(name="content", data_type=DataType.TEXT),
                        Property(name="type", data_type=DataType.TEXT), # body_s, h1, h2
                        Property(name="token_count", data_type=DataType.INT), # Number of tokens in content
                        Property(name="path", data_type=DataType.TEXT), # Source file path
                    ],
                    references=[
                        ReferenceProperty(name="infile", target_collection="sdfile"), # body_s, h1 -> sdfile
                        ReferenceProperty(name="composes", target_collection="sdbody"), # h2 -> h1
                        ReferenceProperty(name="follows", target_collection="sdbody"), # h1 -> body_s
                    ]
                )
                logger.info("Created collection: sdbody")
                
        except Exception as e:
            logger.error(f"Error ensuring schema: {e}")
            raise

    def reset_schema(self):
        """Deletes all collections and recreates them."""
        try:
            self.client.collections.delete("sddir")
            self.client.collections.delete("sdfile")
            self.client.collections.delete("sdbody")
            logger.info("Deleted all collections")
        except Exception as e:
            logger.warning(f"Error deleting collections (might not exist): {e}")
        
        self.ensure_schema()

    def create_sddir(self, name: str, path: str, level: int) -> str:
        collection = self.client.collections.get("sddir")
        
        # Query with limit higher than 1 to catch potential tokenization issues
        from weaviate.classes.query import Filter
        results = collection.query.fetch_objects(
            filters=Filter.by_property("path").equal(path),
            limit=10  # Get more results to filter client-side
        )
        
        # Client-side exact match validation
        uuid = None
        if results.objects:
            for obj in results.objects:
                obj_path = obj.properties.get("path", "")
                if obj_path == path:  # Exact match
                    uuid = str(obj.uuid)
                    logger.debug(f"Found existing dir: {path} -> {uuid[:8]}...")
                    break
        
        # If no exact match found, create new object
        if uuid is None:
            uuid = str(collection.data.insert({
                "name": name,
                "path": path,
                "level": level
            }))
            logger.debug(f"Created new dir: {path} -> {uuid[:8]}...")
        
        return uuid

    def create_sdfile(self, name: str, path: str, dir_uuid: str) -> str:
        collection = self.client.collections.get("sdfile")
        
        # Query with limit higher than 1 to catch potential tokenization issues
        results = collection.query.fetch_objects(
            filters=weaviate.classes.query.Filter.by_property("path").equal(path),
            limit=10  # Get more results to filter client-side
        )
        
        # Client-side exact match validation
        # Weaviate's .equal() may return partial matches due to text tokenization
        uuid = None
        if results.objects:
            for obj in results.objects:
                obj_path = obj.properties.get("path", "")
                if obj_path == path:  # Exact match
                    uuid = str(obj.uuid)
                    logger.debug(f"Found existing file: {path} -> {uuid[:8]}...")
                    break
        
        # If no exact match found, create new object
        if uuid is None:
            uuid = str(collection.data.insert({
                "name": name,
                "path": path
            }))
            logger.debug(f"Created new file: {path} -> {uuid[:8]}...")
        
        # Link to dir
        if dir_uuid:
            collection.data.reference_add(
                from_uuid=uuid,
                from_property="indir",
                to=dir_uuid
            )
        return uuid


    def clear_file_bodies(self, file_uuid: str):
        """
        Deletes all sdbody nodes associated with a file.
        This includes:
        - body_s nodes linked to the file (via infile)
        - h1 nodes linked to the file (via infile)
        - h2 nodes linked to h1 nodes (via composes)
        """
        collection = self.client.collections.get("sdbody")
        from weaviate.classes.query import Filter
        
        bodies_to_delete = set()
        
        # Find all bodies that reference this file via 'infile' (body_s and h1)
        try:
            results = collection.query.fetch_objects(
                filters=Filter.by_ref("infile").by_id().equal(file_uuid),
                limit=10000  # Cap
            )
            
            for obj in results.objects:
                bodies_to_delete.add(str(obj.uuid))
                
                # If this is an h1, find any h2s that compose it
                if obj.properties.get("type") == "h1":
                    h2_results = collection.query.fetch_objects(
                        filters=Filter.by_ref("composes").by_id().equal(str(obj.uuid)),
                        limit=10000
                    )
                    for h2_obj in h2_results.objects:
                        bodies_to_delete.add(str(h2_obj.uuid))
        
        except Exception as e:
            logger.warning(f"Error querying bodies for file {file_uuid}: {e}")
            return
        
        # Batch delete all collected bodies
        if bodies_to_delete:
            logger.info(f"Clearing {len(bodies_to_delete)} old body nodes...")
            try:
                # Use batch delete for better performance
                collection.data.delete_many(
                    where=Filter.by_id().contains_any(list(bodies_to_delete))
                )
                logger.debug(f"Deleted {len(bodies_to_delete)} body nodes for file {file_uuid[:8]}")
            except Exception as e:
                # Fallback to individual deletion if batch fails
                logger.warning(f"Batch delete failed, falling back to individual deletion: {e}")
                for body_uuid in bodies_to_delete:
                    try:
                        collection.data.delete_by_id(body_uuid)
                    except Exception as e:
                        logger.warning(f"Error deleting body {body_uuid[:8]}: {e}")


    def _split_content_into_chunks(self, content: str, max_tokens: int = None) -> List[str]:
        """
        Split content into chunks that fit within token limit.
        Splits at paragraph boundaries to preserve semantic coherence.
        
        Args:
            content: The content to split
            max_tokens: Maximum tokens per chunk (default: self.MAX_TOKENS_PER_CHUNK)
        
        Returns:
            List of content chunks
        """
        if max_tokens is None:
            max_tokens = self.MAX_TOKENS_PER_CHUNK
        
        # Check if content is already within limit
        total_tokens = count_tokens(content)
        if total_tokens <= max_tokens:
            return [content]
        
        logger.info(f"Content has {total_tokens} tokens, splitting into chunks...")
        
        chunks = []
        current_chunk = []
        current_tokens = 0
        
        # Strategy 1: Split by paragraphs (double newline)
        paragraphs = content.split('\n\n')
        
        for para in paragraphs:
            para_tokens = count_tokens(para)
            
            # If single paragraph exceeds limit, need to split it further
            if para_tokens > max_tokens:
                # Flush current chunk if it has content
                if current_chunk:
                    chunks.append('\n\n'.join(current_chunk))
                    current_chunk = []
                    current_tokens = 0
                
                # Strategy 2: Split by single newlines
                lines = para.split('\n')
                for line in lines:
                    line_tokens = count_tokens(line)
                    
                    if line_tokens > max_tokens:
                        # Strategy 3: Split by sentences
                        sentences = re.split(r'([.!?]\s+)', line)
                        sentence_chunk = []
                        sentence_tokens = 0
                        
                        for i in range(0, len(sentences), 2):
                            sentence = sentences[i]
                            if i + 1 < len(sentences):
                                sentence += sentences[i + 1]  # Include delimiter
                            
                            sent_tokens = count_tokens(sentence)
                            
                            if sentence_tokens + sent_tokens > max_tokens and sentence_chunk:
                                chunks.append(''.join(sentence_chunk))
                                sentence_chunk = [sentence]
                                sentence_tokens = sent_tokens
                            else:
                                sentence_chunk.append(sentence)
                                sentence_tokens += sent_tokens
                        
                        if sentence_chunk:
                            chunks.append(''.join(sentence_chunk))
                    else:
                        # Line fits, check if we can add to current chunk
                        if current_tokens + line_tokens > max_tokens and current_chunk:
                            chunks.append('\n'.join(current_chunk))
                            current_chunk = [line]
                            current_tokens = line_tokens
                        else:
                            current_chunk.append(line)
                            current_tokens += line_tokens
                
                # Flush line-level chunk
                if current_chunk:
                    chunks.append('\n'.join(current_chunk))
                    current_chunk = []
                    current_tokens = 0
            else:
                # Paragraph fits, check if we can add to current chunk
                if current_tokens + para_tokens > max_tokens and current_chunk:
                    # Current chunk is full, save it and start new one
                    chunks.append('\n\n'.join(current_chunk))
                    current_chunk = [para]
                    current_tokens = para_tokens
                else:
                    # Add paragraph to current chunk
                    current_chunk.append(para)
                    current_tokens += para_tokens
        
        # Don't forget the last chunk
        if current_chunk:
            chunks.append('\n\n'.join(current_chunk))
        
        logger.info(f"Split into {len(chunks)} chunks")
        return chunks

    def process_file_content(self, file_uuid: str, content: str, file_path: str):
        """
        Parses markdown content and creates sdbody nodes using batch insertion.
        This significantly improves performance by:
        1. Reducing network requests (1 batch insert vs N individual inserts)
        2. Leveraging VoyageAI's batch vectorization API
        
        Args:
            file_uuid: UUID of the sdfile
            content: Markdown content to process
            file_path: Path of the source file (for path property)
        """
        # Clear old body nodes for this file before adding new ones
        self.clear_file_bodies(file_uuid)
        
        lines = content.split('\n')
        
        # Regex for headers
        h1_regex = re.compile(r'^#\s+(.+)$')
        h2_regex = re.compile(r'^##\s+(.+)$')
        
        # Collect all nodes to insert in batch
        nodes_to_insert = []
        
        # Phase 1: Parse document and collect node information
        # ====================================================
        
        # 1. Process body_s (content before first H1)
        body_s_content = []
        first_h1_idx = -1
        
        for i, line in enumerate(lines):
            if h1_regex.match(line):
                first_h1_idx = i
                break
            body_s_content.append(line)
        
        last_body_uuid = None
        if body_s_content:
            body_s_text = "\n".join(body_s_content)
            if body_s_text.strip():  # Only create if non-empty
                # Split body_s content into chunks if needed
                body_chunks = self._split_content_into_chunks(body_s_text)
                
                first_chunk_uuid = None
                prev_chunk_uuid = None
                
                for chunk_idx, chunk_content in enumerate(body_chunks):
                    chunk_uuid = str(uuid.uuid4())
                    
                    if chunk_idx == 0:
                        first_chunk_uuid = chunk_uuid
                    
                    # Determine chunk name
                    if len(body_chunks) > 1:
                        chunk_name = f"body_s_chunk_{chunk_idx + 1}"
                    else:
                        chunk_name = "body_s"
                    
                    # Calculate token count for this chunk
                    chunk_tokens = count_tokens(chunk_content)
                    
                    node_data = {
                        "uuid": chunk_uuid,
                        "properties": {
                            "name": chunk_name,
                            "content": chunk_content,
                            "type": "body_s",
                            "token_count": chunk_tokens,
                            "path": file_path
                        },
                        "references": {}
                    }
                    
                    if chunk_idx == 0:
                        # First chunk links to file
                        node_data["references"]["infile"] = file_uuid
                    else:
                        # Subsequent chunks follow the previous chunk (sequential relationship)
                        # No composes relationship - chunks are at the same level
                        node_data["references"]["follows"] = prev_chunk_uuid
                    
                    nodes_to_insert.append(node_data)
                    prev_chunk_uuid = chunk_uuid
                
                last_body_uuid = first_chunk_uuid
        
        if first_h1_idx == -1:
            # No H1s found, batch insert what we have
            if nodes_to_insert:
                self._batch_insert_nodes(nodes_to_insert)
            return
        
        # 2. Process H1s and H2s
        remaining_lines = lines[first_h1_idx:]
        
        current_h1_uuid = None
        last_h2_uuid = None
        
        current_node_type = None
        current_node_content = []
        current_node_name = None
        
        def flush_node():
            nonlocal current_node_content, current_node_name, current_node_type
            nonlocal last_body_uuid, current_h1_uuid, last_h2_uuid
            
            if current_node_name and current_node_type:
                content_text = "\n".join(current_node_content)
                
                # Split content into chunks if needed
                content_chunks = self._split_content_into_chunks(content_text)
                
                # Track the first chunk UUID to return
                first_chunk_uuid = None
                prev_chunk_uuid = None
                
                for chunk_idx, chunk_content in enumerate(content_chunks):
                    chunk_uuid = str(uuid.uuid4())
                    
                    if chunk_idx == 0:
                        first_chunk_uuid = chunk_uuid
                    
                    # Determine chunk name
                    if len(content_chunks) > 1:
                        chunk_name = f"{current_node_name}_chunk_{chunk_idx + 1}"
                    else:
                        chunk_name = current_node_name
                    
                    # Calculate token count for this chunk
                    chunk_tokens = count_tokens(chunk_content)
                    
                    node_data = {
                        "uuid": chunk_uuid,
                        "properties": {
                            "name": chunk_name,
                            "content": chunk_content,
                            "type": current_node_type,
                            "token_count": chunk_tokens,
                            "path": file_path
                        },
                        "references": {}
                    }
                    
                    if current_node_type == 'h1':
                        if chunk_idx == 0:
                            # First chunk links to file
                            node_data["references"]["infile"] = file_uuid
                            # H1 follows previous H1 or body_s (same level)
                            if last_body_uuid:
                                node_data["references"]["follows"] = last_body_uuid
                        else:
                            # Subsequent chunks follow the previous chunk (sequential relationship)
                            # No composes relationship - chunks are at the same level
                            node_data["references"]["follows"] = prev_chunk_uuid
                        
                    elif current_node_type == 'h2':
                        if chunk_idx == 0:
                            # First chunk composes h1 (hierarchical relationship)
                            if current_h1_uuid:
                                node_data["references"]["composes"] = current_h1_uuid
                            else:
                                logger.warning(f"H2 {current_node_name} found without H1 parent")
                            
                            # h2 follows previous h2 within same h1 (same level)
                            if last_h2_uuid:
                                node_data["references"]["follows"] = last_h2_uuid
                        else:
                            # Subsequent chunks follow the previous chunk (sequential relationship)
                            # No composes relationship - chunks are at the same level
                            node_data["references"]["follows"] = prev_chunk_uuid
                    
                    nodes_to_insert.append(node_data)
                    prev_chunk_uuid = chunk_uuid
                
                # Update tracking variables based on node type
                if current_node_type == 'h1':
                    last_body_uuid = first_chunk_uuid  # Track first chunk for follows
                elif current_node_type == 'h2':
                    last_h2_uuid = first_chunk_uuid  # Track first chunk for follows
                
                return first_chunk_uuid
            return None
        
        for line in remaining_lines:
            h1_match = h1_regex.match(line)
            h2_match = h2_regex.match(line)
            
            if h1_match:
                # Flush previous node
                flushed_uuid = flush_node()
                if current_node_type == 'h1':
                    current_h1_uuid = flushed_uuid
                
                # Start new H1
                current_node_type = 'h1'
                current_node_name = h1_match.group(1)
                current_node_content = [line]
                last_h2_uuid = None  # Reset H2 tracking for new H1
                
            elif h2_match:
                # Flush previous node (could be H1 or H2)
                flushed_uuid = flush_node()
                
                if current_node_type == 'h1':
                    current_h1_uuid = flushed_uuid
                
                # Start new H2
                current_node_type = 'h2'
                current_node_name = h2_match.group(1)
                current_node_content = [line]
                
            else:
                current_node_content.append(line)
        
        # Flush last node
        flush_node()
        
        # Phase 2: Batch insert all nodes
        # ================================
        if nodes_to_insert:
            self._batch_insert_nodes(nodes_to_insert)
    
    def _batch_insert_nodes(self, nodes: List[Dict[str, Any]]):
        """
        Helper method to batch insert nodes with their references.
        Uses a two-phase approach:
        1. Batch insert all nodes (without references)
        2. Batch add all references
        
        This is necessary because Weaviate requires referenced objects to exist
        before adding references, even in a batch operation.
        """
        collection = self.client.collections.get("sdbody")
        
        try:
            # Phase 1: Batch insert all nodes WITHOUT references
            from weaviate.classes.data import DataObject
            
            data_objects = []
            for node in nodes:
                data_obj = DataObject(
                    properties=node["properties"],
                    uuid=node["uuid"]
                    # No references yet
                )
                data_objects.append(data_obj)
            
            # Batch insert nodes
            logger.debug(f"Batch inserting {len(nodes)} nodes...")
            response = collection.data.insert_many(data_objects)
            
            if response.has_errors:
                error_count = sum(1 for err in response.errors.values() if err)
                logger.error(f"Batch insert had {error_count} errors")
                for i, error in response.errors.items():
                    if error:
                        logger.error(f"Error inserting node {i}: {error}")
                # Don't proceed to add references if inserts failed
                return
            else:
                logger.debug(f"Successfully batch inserted {len(nodes)} nodes")
            
            # Phase 2: Batch add all references
            references_to_add = []
            for node in nodes:
                node_uuid =node["uuid"]
                refs = node.get("references", {})
                
                for ref_name, ref_uuid in refs.items():
                    references_to_add.append({
                        "from_uuid": node_uuid,
                        "from_property": ref_name,
                        "to_uuid": ref_uuid
                    })
            
            if references_to_add:
                logger.debug(f"Adding {len(references_to_add)} references...")
                for ref in references_to_add:
                    try:
                        collection.data.reference_add(
                            from_uuid=ref["from_uuid"],
                            from_property=ref["from_property"],
                            to=ref["to_uuid"]
                        )
                    except Exception as ref_error:
                        logger.error(f"Error adding reference {ref['from_property']}: {ref_error}")
                        
        except Exception as e:
            logger.error(f"Batch insert failed: {e}")
            # Fallback to individual inserts if batch fails
            logger.warning("Falling back to individual inserts...")
            for node in nodes:
                try:
                    collection.data.insert(
                        properties=node["properties"],
                        uuid=node["uuid"]
                    )
                    # Add references individually
                    refs = node.get("references", {})
                    for ref_name, ref_uuid in refs.items():
                        try:
                            collection.data.reference_add(
                                from_uuid=node["uuid"],
                                from_property=ref_name,
                                to=ref_uuid
                            )
                        except Exception as ref_error:
                            logger.error(f"Error adding reference {ref_name}: {ref_error}")
                except Exception as insert_error:
                    logger.error(f"Failed to insert node {node['uuid']}: {insert_error}")


