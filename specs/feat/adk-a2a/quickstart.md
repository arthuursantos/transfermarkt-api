# Quickstart: ADK Tools for Transfermarkt Scraping

## Prerequisites

- Python 3.x
- Poetry installed
- Repository cloned and dependencies installed

## Setup

```bash
# Install dependencies (including google-adk)
poetry install --no-root
```

## Usage

### Import individual tools

```python
from app.tools.players import get_player_profile, search_players
from app.tools.clubs import get_club_profile
from app.tools.competitions import search_competitions

# Call a tool directly
result = get_player_profile(player_id="28003")
print(result)  # dict with player profile data

# Search
results = search_players(query="Messi")
print(results)  # dict with search results
```

### Import all tools

```python
from app.tools import ALL_TOOLS

print(len(ALL_TOOLS))  # 13
```

### Use with an ADK Agent

```python
from google.adk.agents import Agent
from app.tools import ALL_TOOLS

agent = Agent(
    name="transfermarkt_agent",
    model="gemini-2.0-flash",
    instruction="You help users find football/soccer data.",
    tools=ALL_TOOLS,
)
```

## Error Handling

Tools return error dicts instead of raising exceptions:

```python
result = get_player_profile(player_id="invalid")
# {"error": "Player not found (ID: invalid)"}
```

## Validation

```bash
# Run tests
pytest tests/tools/

# Quality gates
ruff check .
black --check .
```
