"""Send LLM traces, including prompts and responses, to a hosted Phoenix collector."""

import os

from openinference.instrumentation.openai import OpenAIInstrumentor
from phoenix.otel import register

PHOENIX_ENDPOINT = os.environ.get(
    "PHOENIX_COLLECTOR_ENDPOINT", "https://app.phoenix.arize.com/v1/traces"
)


def start_tracing(service_name: str) -> None:
    tracer_provider = register(
        project_name=service_name,
        endpoint=PHOENIX_ENDPOINT,
        headers={"api_key": os.environ.get("PHOENIX_API_KEY", "")},
    )
    OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)
