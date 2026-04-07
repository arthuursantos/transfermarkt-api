# Tools API Contract

**Date**: 2026-04-02
**Feature**: `feat/adk-a2a`

## Interface

Tools are plain Python functions importable from `app.tools`.
They are consumed by ADK agents via the `tools` parameter.

## Contract per Tool

Each tool function MUST:

1. Accept typed parameters matching the service constructor
2. Return `dict` on success (matching existing schema structure)
3. Return `{"error": "<message>"}` on failure
4. Have a descriptive docstring (1-2 sentences) for LLM discovery

## Tool Signatures

### Players (`app.tools.players`)

```python
def get_player_profile(player_id: str) -> dict:
    """Get the full profile of a football player by their Transfermarkt ID."""

def get_player_market_value(player_id: str) -> dict:
    """Get market value history of a football player."""

def get_player_transfers(player_id: str) -> dict:
    """Get the transfer history of a football player."""

def get_player_stats(player_id: str) -> dict:
    """Get career statistics of a football player."""

def get_player_injuries(player_id: str, page_number: int = 1) -> dict:
    """Get the injury history of a football player."""

def get_player_jersey_numbers(player_id: str) -> dict:
    """Get the jersey number history of a football player."""

def get_player_achievements(player_id: str) -> dict:
    """Get the achievements and titles of a football player."""

def search_players(query: str, page_number: int = 1) -> dict:
    """Search for football players by name on Transfermarkt."""
```

### Clubs (`app.tools.clubs`)

```python
def get_club_profile(club_id: str) -> dict:
    """Get the full profile of a football club by its Transfermarkt ID."""

def get_club_players(club_id: str, season_id: str = None) -> dict:
    """Get the squad/player list of a football club, optionally for a specific season."""

def search_clubs(query: str, page_number: int = 1) -> dict:
    """Search for football clubs by name on Transfermarkt."""
```

### Competitions (`app.tools.competitions`)

```python
def get_competition_clubs(competition_id: str, season_id: str = None) -> dict:
    """Get the clubs participating in a football competition, optionally for a specific season."""

def search_competitions(query: str, page_number: int = 1) -> dict:
    """Search for football competitions by name on Transfermarkt."""
```

## Collection

```python
from app.tools import ALL_TOOLS  # list of all 13 tool functions
```

## Error Contract

On failure (e.g. unknown ID), tools return:

```python
{"error": "Player not found (ID: 99999999)"}
{"error": "Club not found (ID: 99999999)"}
{"error": "An unexpected error occurred: <details>"}
```

Tools MUST NOT raise unhandled exceptions.
