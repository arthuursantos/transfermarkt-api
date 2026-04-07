# Research: ADK Tools for Transfermarkt Scraping

**Date**: 2026-04-02
**Feature**: `feat/adk-a2a`

## R1: Google ADK Tool Definition Mechanism

**Decision**: Use plain Python functions with type hints and docstrings,
auto-wrapped by ADK when passed to an Agent's `tools` list.

**Rationale**: ADK's `FunctionTool` accepts any plain function — no
decorator or class inheritance needed. The function's docstring becomes
the tool description and type hints generate the parameter schema
automatically. This is the lowest-friction approach.

**Alternatives considered**:
- Explicit `FunctionTool(func=...)` wrapping — unnecessary unless
  customizing name/description beyond what docstring provides.
- Subclassing a Tool base class — not supported by ADK; class-based
  tools are only for more complex tool types (LongRunningFunctionTool).

## R2: ADK Tool Error Handling

**Decision**: Catch `HTTPException` from existing services and return
an error dict `{"error": str}` instead of raising.

**Rationale**: ADK tools should return dicts or strings. Unhandled
exceptions are caught by the framework but produce opaque errors.
Returning `{"error": "Player not found (ID: 123)"}` lets the LLM
reason about failures and retry or inform the user.

**Alternatives considered**:
- Let exceptions propagate — produces generic error messages that
  the LLM cannot reason about.
- Return error strings — less structured than dicts; harder for
  the LLM to distinguish error vs. success responses.

## R3: ADK Package and Dependency

**Decision**: Add `google-adk` as a project dependency via Poetry.

**Rationale**: `google-adk` is the official pip package. It provides
`google.adk.tools.FunctionTool` and `google.adk.agents.Agent`.

**Alternatives considered**:
- `google-genai` — lower-level SDK, does not include ADK agent/tool
  framework.

## R4: Tool Function Signature Pattern

**Decision**: Each tool is a plain function that instantiates the
corresponding service dataclass, calls the public method, and returns
the resulting dict.

**Rationale**: The existing services do all work in `__post_init__`
(URL formatting, HTTP fetch, HTML parsing, validation). The public
method (e.g. `get_player_profile()`) extracts data and returns a dict.
The tool function is a thin wrapper:

```python
def get_player_profile(player_id: str) -> dict:
    """Get the profile of a football player from Transfermarkt."""
    tfmkt = TransfermarktPlayerProfile(player_id=player_id)
    return tfmkt.get_player_profile()
```

Error handling wraps the body in try/except for `HTTPException`.

**Alternatives considered**:
- Returning Pydantic model instances — ADK expects dict/str returns;
  `.model_dump()` would work but adds unnecessary coupling.
- Creating a generic wrapper factory — viable but premature
  abstraction for 13 functions with slightly different signatures.

## R5: Tool Organization

**Decision**: One module per domain under `app/tools/`:
- `app/tools/players.py` — 8 tool functions
- `app/tools/clubs.py` — 3 tool functions
- `app/tools/competitions.py` — 2 tool functions
- `app/tools/__init__.py` — exports `ALL_TOOLS` list for agent consumption

**Rationale**: Mirrors the existing `app/services/` domain structure.
A single `__init__.py` collecting all tools makes agent registration
trivial (`tools=ALL_TOOLS`).

**Alternatives considered**:
- Single `app/tools.py` file — 13 functions in one file is manageable
  but loses domain grouping.
- One file per tool — excessive for simple wrapper functions.
