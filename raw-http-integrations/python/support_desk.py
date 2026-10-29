"""Reply to website visitors in the support chat."""

import base64
import os

import aiohttp


class SupportDesk:
    def __init__(self, website_id: str) -> None:
        self.website_id = website_id
        self.api_root = "https://api.crisp.chat/v1"
        credentials = f"{os.environ['CRISP_IDENTIFIER']}:{os.environ['CRISP_KEY']}"
        self.headers = {
            "Authorization": "Basic " + base64.b64encode(credentials.encode()).decode(),
        }

    def _url(self, path: str) -> str:
        return f"{self.api_root}/website/{self.website_id}/{path}"

    async def reply(self, session_id: str, text: str) -> None:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            await session.post(
                self._url(f"conversation/{session_id}/message"),
                json={"type": "text", "from": "operator", "origin": "chat", "content": text},
            )

    async def visitor_profile(self, session_id: str) -> dict:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(self._url(f"conversation/{session_id}/meta")) as response:
                body = await response.json()
                return {"email": body["data"].get("email"), "nickname": body["data"].get("nickname")}
