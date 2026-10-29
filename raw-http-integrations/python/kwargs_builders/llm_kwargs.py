"""Completion arguments are assembled in helpers and unpacked into the call."""

import litellm
from google.adk.models.lite_llm import LiteLlm

from .config import Config


def gateway_kwargs() -> dict:
    return {"model": Config.GATEWAY_MODEL, "api_base": Config.GATEWAY_BASE_URL}


async def complete(messages: list[dict], **overrides) -> str:
    kwargs = {**gateway_kwargs(), **overrides}
    response = await litellm.acompletion(messages=messages, **kwargs)
    return response.choices[0].message.content


def agent_model() -> LiteLlm:
    return LiteLlm(model=Config.PRIMARY_MODEL)
