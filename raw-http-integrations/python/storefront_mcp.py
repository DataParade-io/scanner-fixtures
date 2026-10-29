"""Search a store's catalogue and add items to a cart through its Storefront MCP server."""

import os

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

SHOP_DOMAIN = os.environ.get("SHOP_DOMAIN", "example-store.myshopify.com")


def storefront_mcp_url(shop: str) -> str:
    return f"https://{shop}/api/mcp"


async def add_to_cart(query: str, quantity: int, buyer_email: str) -> dict:
    async with streamablehttp_client(storefront_mcp_url(SHOP_DOMAIN)) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            found = await session.call_tool("search_shop_catalog", {"query": query})
            variant_id = found.structuredContent["products"][0]["variants"][0]["id"]
            cart = await session.call_tool(
                "update_cart",
                {
                    "add_items": [{"product_variant_id": variant_id, "quantity": quantity}],
                    "buyer_identity": {"email": buyer_email},
                },
            )
            return cart.structuredContent
