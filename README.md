# transfermarkt-api (A2A Agent)

Fork of [felipeall/transfermarkt-api](https://github.com/felipeall/transfermarkt-api), a FastAPI application that scrapes football data from [Transfermarkt](https://www.transfermarkt.com/) and exposes it as structured JSON endpoints.

This fork wraps those scraping services as LLM tools and exposes a football data agent via [A2A protocol](https://google.github.io/A2A/) and [Google ADK](https://google.github.io/adk-docs/), ready for consumption by other agents or AI applications.

---

## Running the A2A Agent

### Prerequisites

- [uv](https://docs.astral.sh/uv/) installed
- An [OpenRouter](https://openrouter.ai/) API key

### Steps

```bash
# Clone the repository
$ git clone https://github.com/arthursantos/transfermarkt-api.git
$ cd transfermarkt-api

# Install dependencies
$ uv sync

# Configure environment variables
$ cp .env.example .env
# Edit .env and set your OPENROUTER_API_KEY

# Start the A2A agent server (localhost:8001)
$ uv run uvicorn app.agent:remote --host localhost --port 8001

# The agent card is available at:
# GET http://localhost:8001/.well-known/agent-card.json
#
# Send JSON-RPC 2.0 requests to:
# POST http://localhost:8001/
```

---

## Running the REST API

The original REST API is still available:

```bash
# Install dependencies
$ uv sync

# Start the API server
$ uv run python app/main.py

# Access the API local page
$ open http://localhost:8000/
```

### Via Docker

```bash
$ docker build -t transfermarkt-api .
$ docker run -d -p 8000:8000 transfermarkt-api
$ open http://localhost:8000/
```

---

## Environment Variables

| Variable                  | Description                                               | Default      |
|---------------------------|-----------------------------------------------------------|--------------|
| `RATE_LIMITING_ENABLE`    | Enable rate limiting feature for API calls                | `false`      |
| `RATE_LIMITING_FREQUENCY` | Delay allowed between each API call. See [slowapi](https://slowapi.readthedocs.io/en/latest/) for more | `2/3seconds` |
| `OPENROUTER_API_KEY`      | API key for OpenRouter (required for A2A agent)           | —            |
| `OPENROUTER_BASE_URL`     | OpenRouter API base URL                                   | `https://openrouter.ai/api/v1` |
