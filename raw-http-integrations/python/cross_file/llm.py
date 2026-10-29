"""Chat completions through two providers whose endpoints live in settings."""

from openai import AsyncOpenAI

from .settings import settings

fast = AsyncOpenAI(base_url=settings.FAST_LLM_BASE_URL, api_key=settings.FAST_LLM_API_KEY)
router = AsyncOpenAI(base_url=settings.ROUTER_BASE_URL, api_key=settings.ROUTER_API_KEY)


async def summarize(transcript: str) -> str:
    result = await fast.chat.completions.create(
        model="llama3.1-8b",
        messages=[{"role": "user", "content": f"Summarize:\n{transcript}"}],
    )
    return result.choices[0].message.content or ""


async def draft_reply(customer_message: str) -> str:
    result = await router.chat.completions.create(
        model="mistralai/mistral-small",
        messages=[{"role": "user", "content": customer_message}],
    )
    return result.choices[0].message.content or ""
