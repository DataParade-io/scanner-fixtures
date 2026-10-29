"""Report completed sign-ups to Meta as server-side conversion events."""

import hashlib
import os
import time

import httpx

PIXEL_ID = os.environ.get("META_PIXEL_ID", "")
CAPI_TOKEN = os.environ.get("META_CAPI_TOKEN", "")
GRAPH_VERSION = "v21.0"
CONVERSIONS_URL = (
    f"https://graph.facebook.com/{GRAPH_VERSION}/{PIXEL_ID}/events?access_token={CAPI_TOKEN}"
)


def _hash(value: str) -> str:
    return hashlib.sha256(value.strip().lower().encode()).hexdigest()


async def report_signup(email: str, phone: str, client_ip: str, user_agent: str) -> bool:
    event = {
        "event_name": "CompleteRegistration",
        "event_time": int(time.time()),
        "action_source": "website",
        "user_data": {
            "em": [_hash(email)],
            "ph": [_hash(phone)],
            "client_ip_address": client_ip,
            "client_user_agent": user_agent,
        },
    }
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.post(CONVERSIONS_URL, json={"data": [event]})
    return response.status_code == 200
