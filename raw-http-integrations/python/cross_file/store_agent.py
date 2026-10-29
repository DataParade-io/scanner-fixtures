"""Give an agent the storefront's MCP tools; the URL is built in shopify_store."""

from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset

from .shopify_store import ShopifyStore


def storefront_tools(store: ShopifyStore) -> McpToolset:
    return McpToolset(connection_params=StreamableHTTPServerParams(url=store.mcp_endpoint()))
