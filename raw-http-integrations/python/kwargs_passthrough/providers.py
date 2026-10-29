"""Choose the LLM backend at runtime; each branch returns its own completion arguments."""

import os

LLM_BACKEND = os.getenv("LLM_BACKEND", "gateway")
GATEWAY_URL = os.getenv("GATEWAY_URL", "https://openrouter.ai/api/v1")
DIRECT_URL = os.getenv("DIRECT_URL", "https://api.cerebras.ai/v1")
MODEL = os.getenv("LLM_MODEL", "gpt-oss-120b")


def completion_kwargs() -> dict:
    if LLM_BACKEND == "gateway":
        return {"model": f"openrouter/openai/{MODEL}", "api_base": GATEWAY_URL}
    return {"model": f"cerebras/{MODEL}", "api_base": DIRECT_URL}
