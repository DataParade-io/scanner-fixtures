"""Route chat completions to a fast or a broad model provider."""

import os

from openai import AsyncOpenAI

fast_client = AsyncOpenAI(
    base_url="https://api.cerebras.ai/v1",
    api_key=os.environ.get("CEREBRAS_API_KEY", ""),
)

broad_client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY", ""),
)


async def answer(user_message: str, conversation: list[dict], prefer_fast: bool) -> str:
    client = fast_client if prefer_fast else broad_client
    model = "llama-3.3-70b" if prefer_fast else "anthropic/claude-sonnet-4"
    completion = await client.chat.completions.create(
        model=model,
        messages=[*conversation, {"role": "user", "content": user_message}],
    )
    return completion.choices[0].message.content or ""
