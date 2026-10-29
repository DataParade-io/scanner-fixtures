"""Triage a support ticket with whichever backend is configured."""

from .llm_client import call_model
from .providers import completion_kwargs


async def triage(ticket_text: str, customer_email: str) -> str:
    response = await call_model(
        **completion_kwargs(),
        temperature=0,
        messages=[{"role": "user", "content": f"From {customer_email}:\n{ticket_text}"}],
    )
    return response.choices[0].message.content
