"""Notify a customer in Telegram, retrying transient failures."""

import os

import httpx
from httpx_retries import Retry, RetryTransport

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")

_retry = Retry(total=4, backoff_factor=0.5, status_forcelist=(429, 500, 502, 503, 504))


async def notify_customer(chat_id: int, text: str) -> None:
    async with httpx.AsyncClient(transport=RetryTransport(retry=_retry), timeout=10) as client:
        await client.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": chat_id, "text": text},
        )
