# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A FastAPI web scraping API that extracts football/soccer data from Transfermarkt.com and exposes it as structured JSON endpoints. Deployed on Fly.io.

## Commands

```bash
# Install all dependencies (including dev groups)
uv sync

# Run the API server locally (localhost:8000)
uv run python app/main.py

# Run the A2A agent server (localhost:8001)
uv run uvicorn app.agent:remote --host localhost --port 8001

# Run all tests (includes coverage, exits on first failure)
uv run --group tests pytest

# Run a single test file
uv run --group tests pytest tests/players/test_players_profile.py

# Linting & formatting
uv run --group check ruff check .
uv run --group check black --check .
uv run --group check black .
uv run --group check interrogate app/services -vv   # docstring coverage, must be 100%
```

## Architecture

**Three-layer pattern: Endpoint → Service → Schema**

- **Endpoints** (`app/api/endpoints/`) — Thin FastAPI route handlers. Each creates a service instance and calls its extraction method.
- **Services** (`app/services/`) — Inherit from `TransfermarktBase` (`app/services/base.py`). Fetch and parse Transfermarkt HTML pages in `__post_init__`, then extract data via XPath. Each domain (players, clubs, competitions) has its own service subdirectory.
- **Schemas** (`app/schemas/`) — Pydantic v2 models with field validators that handle type conversion (currency strings → int, date strings → date, height strings → int). Base model uses camelCase aliases and includes `AuditMixin` for `updated_at` timestamps.

**A2A Agent layer (`app/agent/`):**
- `app/agent/agent.py` — Defines a Google ADK `Agent` with OpenRouter model + Transfermarkt tools, and exposes it via A2A protocol using `to_a2a()`
- `app/agent/__init__.py` — Re-exports `agent` and `remote` (the ASGI app)
- `app/tools/` — ADK-compatible tool functions wrapping the existing services (players, clubs, competitions)
- The A2A server auto-generates an Agent Card at `GET /.well-known/agent-card.json` and accepts JSON-RPC 2.0 requests at `POST /`
- Requires `google-adk[a2a]` (the `[a2a]` extra installs `a2a-sdk`)

**Key utility files:**
- `app/utils/xpath.py` — Centralized XPath selectors as class constants, organized by domain
- `app/utils/regex.py` — Regex patterns for parsing scraped text
- `app/utils/utils.py` — Shared helper functions

**Base class (`TransfermarktBase`) key methods:**
- `request_url_page()` — Fetch URL and parse to lxml ElementTree
- `get_text_by_xpath()` — Extract text from parsed page with optional slicing
- `get_list_by_xpath()` — Extract list of elements by XPath
- `raise_exception_if_not_found()` — Validate page loaded (raises HTTPException 404/500)

## Code Style

- Line length: 120 characters (black + ruff)
- Ruff rules: pyflakes, pycodestyle, isort, flake8-commas, flake8-quotes, fastapi
- All service classes require docstrings (interrogate, 100% coverage on `app/services/`)
- Response models use `response_model_exclude_none=True`

## Testing

Tests hit live Transfermarkt pages (no mocking). They validate response structure using the `schema` library against known player/club/competition IDs. Fixtures in `tests/conftest.py` provide reusable validators (regex matchers, length checks).

## Active Technologies
- Python 3.13 + FastAPI (REST API) + google-adk[a2a] (A2A agent)
- Dependency management: uv (pyproject.toml + uv.lock)
