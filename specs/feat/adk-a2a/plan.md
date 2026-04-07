# Implementation Plan: ADK Tools for Transfermarkt Scraping

**Branch**: `feat/adk-a2a` | **Date**: 2026-04-02 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/feat/adk-a2a/spec.md`

## Summary

Wrap all 13 existing Transfermarkt scraping services as plain Python
functions consumable by Google ADK agents. Each tool function
instantiates the corresponding service dataclass, calls its public
method, and returns the result dict. Tools are organized by domain
(`players`, `clubs`, `competitions`) under `app/tools/`, with an
`__init__.py` exporting `ALL_TOOLS` for agent registration.

## Technical Context

**Language/Version**: Python 3.x
**Primary Dependencies**: FastAPI (existing), google-adk (new)
**Storage**: N/A
**Testing**: pytest (existing framework, live Transfermarkt pages)
**Target Platform**: Linux server (Fly.io)
**Project Type**: web-service + ADK tool layer
**Performance Goals**: Same as existing API (tools reuse services)
**Constraints**: Tools must not modify existing service/schema code
**Scale/Scope**: 13 tool functions across 3 domain modules

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. SDD | PASS | Spec and plan created before implementation |
| II. TDD | PASS | Tests will be written before tool implementations |
| III. Three-Layer Architecture | PASS | Tools are a new parallel layer (`app/tools/`), not replacing or bypassing Endpoint→Service→Schema |
| IV. Code Quality Gates | PASS | All gates will be enforced (ruff, black, interrogate on services, pytest) |
| V. Live Data Testing | PASS | Tool tests will hit live Transfermarkt pages, no mocking |

## Project Structure

### Documentation (this feature)

```text
specs/feat/adk-a2a/
├── spec.md
├── plan.md              # This file
├── research.md
├── data-model.md
├── quickstart.md
└── contracts/
    └── tools-api.md
```

### Source Code (repository root)

```text
app/
├── tools/
│   ├── __init__.py          # ALL_TOOLS list export
│   ├── players.py           # 8 player tool functions
│   ├── clubs.py             # 3 club tool functions
│   └── competitions.py      # 2 competition tool functions
├── services/                # UNCHANGED
├── schemas/                 # UNCHANGED
└── api/endpoints/           # UNCHANGED

tests/
└── tools/
    ├── __init__.py
    ├── test_tools_players.py
    ├── test_tools_clubs.py
    └── test_tools_competitions.py
```

**Structure Decision**: New `app/tools/` package mirrors `app/services/`
domain structure. Existing code is untouched.

## Complexity Tracking

No constitution violations to justify.
