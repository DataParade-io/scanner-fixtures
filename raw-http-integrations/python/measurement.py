"""Send a server-side purchase event to Google Analytics."""

import os

import requests

MEASUREMENT_ID = os.environ.get("GA_MEASUREMENT_ID", "")
API_SECRET = os.environ.get("GA_API_SECRET", "")
COLLECT_ENDPOINT = (
    "https://www.google-analytics.com/mp/collect"
    f"?measurement_id={MEASUREMENT_ID}&api_secret={API_SECRET}"
)


def track_purchase(client_id: str, user_id: str, order_id: str, total: float, currency: str) -> None:
    payload = {
        "client_id": client_id,
        "user_id": user_id,
        "events": [
            {
                "name": "purchase",
                "params": {"transaction_id": order_id, "value": total, "currency": currency},
            }
        ],
    }
    requests.post(COLLECT_ENDPOINT, json=payload, timeout=5)
