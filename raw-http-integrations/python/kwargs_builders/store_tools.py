"""Catalog tools for a Shopify store; the MCP URL passes through a kwargs dict."""

from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset


def _connection(url: str, timeout: float) -> StreamableHTTPServerParams:
    params = {"url": url, "timeout": timeout}
    return StreamableHTTPServerParams(**params)


class ShopifyCatalogTools:
    def __init__(self, shop: str, url_override: str | None = None) -> None:
        endpoint = url_override or f"https://{shop}/api/mcp"
        self.toolset = McpToolset(connection_params=_connection(url=endpoint, timeout=20))
