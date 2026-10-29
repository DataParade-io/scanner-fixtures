"""Thin wrapper that forwards every argument to LiteLLM and retries on rate limits."""

import litellm


async def call_model(**kwargs):
    try:
        return await litellm.acompletion(**kwargs)
    except litellm.exceptions.RateLimitError:
        return await litellm.acompletion(**{**kwargs, "num_retries": 2})
