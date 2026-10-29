# scanner-fixtures

Small, original code examples for evaluating the [DataParade](https://dataparade.io) scanner.

Each folder shows one family of code patterns that a privacy and data-flow scanner must handle. The code is written to be read, not run: it is short, it has no tests, and it reads every credential from the environment. Gold labels for these files live in the scanner's evaluation corpus, not here.

| Folder | What it shows |
| --- | --- |
| [`raw-http-integrations/`](raw-http-integrations/) | Third-party services called with a raw HTTP client (httpx, aiohttp, requests) or an OpenAI-compatible client, instead of the vendor's SDK |

## Adding examples

- Write new code. Do not copy code from other projects, open or closed.
- One pattern per file, named for what the code does.
- Read credentials from environment variables. Never commit a real key, token or webhook URL.
- Say in the folder README which pattern each file shows and which services it reaches.

## Licence

MIT. See [LICENSE](LICENSE).
