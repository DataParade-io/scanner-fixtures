# Raw-HTTP integrations

Applications often call a vendor's REST API directly with an HTTP client instead of the vendor's SDK. A scanner that only recognises SDK imports misses these services, and may report the HTTP client library itself as the destination. The library is never the destination; the host in the URL is.

| File | Pattern | Service reached |
| --- | --- | --- |
| `python/ad_conversions.py` | URL built in a module constant, credential in the query string, posted with httpx | Meta Conversions API (`graph.facebook.com`) |
| `python/measurement.py` | Credentials in the query string of a module constant, sent with requests | Google Analytics Measurement Protocol |
| `python/lead_webhook.py` | Automation-platform webhook URL read from the environment, with a default host | Make.com |
| `python/storefront_mcp.py` | Remote MCP server over streamable HTTP, URL built from a shop domain | Shopify Storefront MCP |
| `python/notify_with_retries.py` | httpx client wrapped in a retry transport, full URL in the call | Telegram Bot API |
| `python/llm_router.py` | OpenAI client pointed at other providers with `base_url` | OpenRouter, Cerebras |
| `python/tracing.py` | Trace exporter sent to a hosted collector endpoint | Arize Phoenix |
| `python/support_desk.py` | Base URL stored on the class, aiohttp session, relative paths joined later | Crisp |
| `python/outbound_unknown.py` | URL comes only from configuration, so the host is not known | Unknown outbound HTTP |
| `python/cross_file/llm.py` + `settings.py` | OpenAI clients whose `base_url` comes from a settings class in another module | Cerebras, OpenRouter |
| `python/cross_file/model_prefixes.py` | LiteLLM model strings with a provider prefix, no URL in the code | Together AI, Groq |
| `python/cross_file/tracing_setup.py` | Vendor package import (`phoenix.otel`), endpoint from settings with no default | Arize Phoenix |
| `python/cross_file/store_agent.py` + `shopify_store.py` | MCP URL `https://{domain}/api/mcp` built by a method in another module, passed to Google ADK | Shopify Storefront MCP |
| `python/kwargs_builders/llm_kwargs.py` + `config.py` | LiteLLM `model` and `api_base` assembled in a helper dict and unpacked with `**kwargs`; Google ADK `LiteLlm(model=...)`; defaults wrapped in a validator call | OpenRouter, Cerebras |
| `python/kwargs_builders/store_tools.py` | MCP URL passed through a helper parameter into a dict, then `StreamableHTTPServerParams(**params)` | Shopify Storefront MCP |

`python/http_helpers.py` is a shared wrapper around httpx. It sends data nowhere by itself.
