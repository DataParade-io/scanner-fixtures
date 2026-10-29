"""Forward a new sales lead to an automation scenario."""

import os
from dataclasses import asdict, dataclass

import requests

LEAD_HOOK_URL = os.environ.get("LEAD_HOOK_URL", "https://hook.eu1.make.com/replace-with-scenario-id")
LEAD_HOOK_KEY = os.environ.get("LEAD_HOOK_KEY", "")


@dataclass
class Lead:
    full_name: str
    email: str
    phone: str
    company: str
    message: str


def forward_lead(lead: Lead) -> None:
    response = requests.post(
        LEAD_HOOK_URL,
        json=asdict(lead),
        headers={"x-make-apikey": LEAD_HOOK_KEY},
        timeout=10,
    )
    response.raise_for_status()
