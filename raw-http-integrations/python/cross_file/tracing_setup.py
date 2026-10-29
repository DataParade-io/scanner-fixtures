"""Export spans with the Phoenix package; the endpoint comes from settings."""

from opentelemetry.sdk.trace import TracerProvider
import phoenix.otel

from .settings import settings


def install_tracing() -> TracerProvider:
    provider = TracerProvider()
    if settings.TRACES_ENDPOINT:
        provider.add_span_processor(phoenix.otel.BatchSpanProcessor(endpoint=settings.TRACES_ENDPOINT))
    return provider
