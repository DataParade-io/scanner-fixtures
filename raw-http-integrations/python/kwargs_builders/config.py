"""Model and gateway settings, validated at import time."""

import os

from pydantic import TypeAdapter


class Config:
    PRIMARY_MODEL = TypeAdapter(str).validate_python(os.getenv("PRIMARY_MODEL", "cerebras/qwen-3-32b"))
    GATEWAY_BASE_URL = TypeAdapter(str).validate_python(
        os.getenv("GATEWAY_BASE_URL", "https://openrouter.ai/api/v1")
    )
    GATEWAY_MODEL = TypeAdapter(str).validate_python(os.getenv("GATEWAY_MODEL", "openrouter/qwen/qwen3-32b"))
