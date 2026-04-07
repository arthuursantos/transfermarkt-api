# Data Model: ADK Tools for Transfermarkt Scraping

**Date**: 2026-04-02
**Feature**: `feat/adk-a2a`

## Overview

This feature introduces no new data entities. Tools are stateless
functions that delegate to existing service classes and return
existing schema-compatible dicts.

## Entities (existing, unchanged)

### Service Classes (data source)

All services are `@dataclass` subclasses of `TransfermarktBase`:

| Service | Domain | Init Fields | Public Method |
|---------|--------|-------------|---------------|
| TransfermarktPlayerProfile | players | player_id | get_player_profile() → dict |
| TransfermarktPlayerMarketValue | players | player_id | get_player_market_value() → dict |
| TransfermarktPlayerTransfers | players | player_id | get_player_transfers() → dict |
| TransfermarktPlayerStats | players | player_id | get_player_stats() → dict |
| TransfermarktPlayerInjuries | players | player_id, page_number=1 | get_player_injuries() → dict |
| TransfermarktPlayerJerseyNumbers | players | player_id | get_player_jersey_numbers() → dict |
| TransfermarktPlayerAchievements | players | player_id | get_player_achievements() → dict |
| TransfermarktPlayerSearch | players | query, page_number=1 | search_players() → dict |
| TransfermarktClubProfile | clubs | club_id | get_club_profile() → dict |
| TransfermarktClubPlayers | clubs | club_id, season_id=None | get_club_players() → dict |
| TransfermarktClubSearch | clubs | query, page_number=1 | search_clubs() → dict |
| TransfermarktCompetitionClubs | competitions | competition_id, season_id=None | get_competition_clubs() → dict |
| TransfermarktCompetitionSearch | competitions | query, page_number=1 | search_competitions() → dict |

### Tool Functions (new, wrapping services)

Each tool is a plain Python function with:
- **Input**: Same parameters as service init fields (type-hinted)
- **Output**: `dict` (success) or `dict` with `"error"` key (failure)
- **Docstring**: Used by ADK for tool discovery and LLM prompting

No new Pydantic models, database tables, or state is introduced.

## Relationships

```
Tool Function → instantiates → Service Dataclass → returns → dict
                                    ↓
                              TransfermarktBase
                                    ↓
                              HTTP fetch + XPath parse
```
