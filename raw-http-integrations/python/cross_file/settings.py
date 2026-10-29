"""Central settings. Other modules read provider endpoints from here."""

import os


class Settings:
    FAST_LLM_BASE_URL = os.environ.get("FAST_LLM_BASE_URL", "https://api.cerebras.ai/v1")
    FAST_LLM_API_KEY = os.environ.get("FAST_LLM_API_KEY", "")
    ROUTER_BASE_URL = os.environ.get("ROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    ROUTER_API_KEY = os.environ.get("ROUTER_API_KEY", "")
    TRACES_ENDPOINT = os.environ.get("TRACES_ENDPOINT", "")


settings = Settings()
