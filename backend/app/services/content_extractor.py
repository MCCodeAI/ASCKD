import httpx
import trafilatura
import logging
import asyncio
from typing import Optional

logger = logging.getLogger(__name__)

async def fetch_and_extract(url: str, timeout: int = 10) -> Optional[str]:
    """
    Fetch a URL and extract its main content using trafilatura.
    Returns None if fetching or extraction fails.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        async with httpx.AsyncClient(follow_redirects=True, verify=False, headers=headers) as client:
            response = await client.get(url, timeout=timeout)
            response.raise_for_status()
            
            # Extract content
            downloaded = response.text
            result = trafilatura.extract(
                downloaded,
                url=url,
                include_comments=False,
                include_tables=True,
                include_images=True,
                output_format="html",
                no_fallback=False
            )
            
            if result:
                return result
            else:
                logger.warning(f"Trafilatura could not extract content from {url}")
                return None
                
    except Exception as e:
        logger.warning(f"Failed to fetch/extract {url}: {e}")
        return None

async def batch_fetch_and_extract(urls: list[str], timeout: int = 10) -> dict[str, str]:
    """
    Fetch and extract content for multiple URLs in parallel.
    Returns a dict mapping URL to extracted content.
    """
    tasks = [fetch_and_extract(url, timeout) for url in urls]
    results = await asyncio.gather(*tasks)
    
    return {
        url: content 
        for url, content in zip(urls, results) 
        if content is not None
    }
