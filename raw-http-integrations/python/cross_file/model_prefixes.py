"""Pick a provider by LiteLLM model prefix; no URL appears in the code."""

import litellm

PROVIDER_MODELS = {
    "cheap": "openrouter/google/gemma-3-27b-it",
    "fast": "cerebras/llama3.1-8b",
}


async def classify(ticket_text: str, tier: str) -> str:
    response = await litellm.acompletion(
        model=PROVIDER_MODELS[tier],
        messages=[{"role": "user", "content": f"Classify this support ticket:\n{ticket_text}"}],
    )
    return response.choices[0].message.content
