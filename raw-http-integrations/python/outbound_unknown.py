"""Push account changes to whatever endpoint the operator configured."""

import os

from http_helpers import post_json

ACCOUNT_SYNC_URL = os.environ["ACCOUNT_SYNC_URL"]


async def sync_account(user_id: str, email: str, display_name: str) -> None:
    await post_json(ACCOUNT_SYNC_URL, {"id": user_id, "email": email, "name": display_name})
