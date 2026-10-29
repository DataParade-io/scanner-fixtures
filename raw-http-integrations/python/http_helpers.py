"""Shared JSON-over-HTTP helper. It has no destination of its own."""

import httpx


async def post_json(url: str, body: dict, timeout: float = 10.0) -> dict:
    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.post(url, json=body)
        response.raise_for_status()
        return response.json()
