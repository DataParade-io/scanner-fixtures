"""Web research tools that call two APIs whose vendor names differ from their hosts."""

import os

import httpx


async def ask_with_sources(question: str) -> str:
    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(
            "https://api.perplexity.ai/chat/completions",
            headers={"Authorization": f"Bearer {os.environ['PERPLEXITY_API_KEY']}"},
            json={"model": "sonar", "messages": [{"role": "user", "content": question}]},
        )
    return response.json()["choices"][0]["message"]["content"]


async def fetch_page_markdown(url: str) -> str:
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(
            "https://api.firecrawl.dev/v1/scrape",
            headers={"Authorization": f"Bearer {os.environ['FIRECRAWL_API_KEY']}"},
            json={"url": url, "formats": ["markdown"]},
        )
    return response.json()["data"]["markdown"]
