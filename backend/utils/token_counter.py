"""
Token counting utility for content chunking.
Uses tiktoken to count tokens in text content.
"""
import tiktoken
from typing import Optional


def count_tokens(text: str, encoding_name: str = "cl100k_base") -> int:
    """
    Count the number of tokens in a text string.
    
    Args:
        text: The text to count tokens for
        encoding_name: The tokenizer encoding to use (default: cl100k_base)
                      cl100k_base is used by GPT-4 and many modern embedding models
    
    Returns:
        Number of tokens in the text
    """
    try:
        encoding = tiktoken.get_encoding(encoding_name)
        tokens = encoding.encode(text)
        return len(tokens)
    except Exception as e:
        # Fallback: rough estimate based on characters
        # Typically ~4 characters per token for English text
        print(f"Warning: Token counting failed ({e}), using character-based estimate")
        return len(text) // 4


def estimate_tokens(text: str) -> int:
    """
    Quick token estimate without loading tiktoken.
    Useful for performance-critical paths.
    
    Args:
        text: The text to estimate tokens for
    
    Returns:
        Estimated number of tokens (roughly 4 chars per token)
    """
    return len(text) // 4
