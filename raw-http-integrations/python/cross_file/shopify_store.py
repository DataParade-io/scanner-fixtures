"""Connection details for a merchant's Shopify storefront."""

from dataclasses import dataclass


@dataclass
class ShopifyStore:
    domain: str
    endpoint_override: str | None = None

    def mcp_endpoint(self) -> str:
        return self.endpoint_override or f"https://{self.domain}/api/mcp"
