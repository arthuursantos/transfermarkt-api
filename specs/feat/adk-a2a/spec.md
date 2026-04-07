# Feature Specification: ADK Tools for Transfermarkt Scraping

**Feature Branch**: `feat/adk-a2a`
**Created**: 2026-04-02
**Status**: Draft
**Input**: User description: "Transform existing Transfermarkt scraping service methods into Google ADK tools"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Invoke a Player Tool (Priority: P1)

An ADK agent invokes a player-domain tool (e.g. get player profile)
by passing a player ID. The tool executes the existing scraping
logic and returns structured JSON matching the current API schema.

**Why this priority**: Player tools cover 8 of 13 services and
represent the most data-rich domain. Proving the pattern here
validates the approach for all other domains.

**Independent Test**: Invoke the player profile tool with a known
player ID and verify the returned JSON matches the expected Pydantic
schema structure.

**Acceptance Scenarios**:

1. **Given** a valid player ID, **When** the get-player-profile tool
   is invoked, **Then** it returns a JSON object matching the player
   profile schema with all expected fields populated.
2. **Given** a valid player ID, **When** the get-player-market-value
   tool is invoked, **Then** it returns market value history as a
   JSON array with date, value, and club for each entry.
3. **Given** an invalid player ID, **When** any player tool is
   invoked, **Then** it returns a clear error indicating the player
   was not found.

---

### User Story 2 - Invoke a Club Tool (Priority: P2)

An ADK agent invokes a club-domain tool (e.g. get club profile,
get club players) by passing a club ID and optional season. The
tool returns structured JSON.

**Why this priority**: Club tools (3 services) are the second
largest domain and depend on a similar wrapping pattern validated
in US1.

**Independent Test**: Invoke the club profile tool with a known
club ID and verify the response matches the club profile schema.

**Acceptance Scenarios**:

1. **Given** a valid club ID, **When** the get-club-profile tool is
   invoked, **Then** it returns club profile data as structured JSON.
2. **Given** a valid club ID and season, **When** the get-club-players
   tool is invoked, **Then** it returns a list of players for that
   season.
3. **Given** a search query, **When** the search-clubs tool is
   invoked, **Then** it returns matching clubs with pagination support.

---

### User Story 3 - Invoke a Competition Tool (Priority: P3)

An ADK agent invokes a competition-domain tool (e.g. search
competitions, get competition clubs) by passing appropriate
parameters. The tool returns structured JSON.

**Why this priority**: Competition tools (2 services) are the
smallest domain and follow the same wrapping pattern.

**Independent Test**: Invoke the search-competitions tool with
a known query and verify results match the competition search schema.

**Acceptance Scenarios**:

1. **Given** a search query, **When** the search-competitions tool
   is invoked, **Then** it returns matching competitions as JSON.
2. **Given** a competition ID and optional season, **When** the
   get-competition-clubs tool is invoked, **Then** it returns clubs
   participating in that competition.

---

### Edge Cases

- What happens when the Transfermarkt page is temporarily unavailable?
- How does the tool behave when optional parameters (season, page)
  are omitted?
- What happens when a valid ID returns a page with missing/partial
  data fields?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST expose each of the 13 existing scraping
  services as an individual ADK tool.
- **FR-002**: Each tool MUST accept the same input parameters as
  the corresponding service class constructor (e.g. `player_id`,
  `club_id`, `query`, `page_number`, `season_id`).
- **FR-003**: Each tool MUST return structured JSON output matching
  the existing Pydantic response schema for that service.
- **FR-004**: Tools MUST be organized by domain: players (8 tools),
  clubs (3 tools), competitions (2 tools).
- **FR-005**: Each tool MUST have a descriptive name and docstring
  so an ADK agent can discover and understand its purpose.
- **FR-006**: Tools MUST propagate errors from the underlying
  services (e.g. 404 for unknown IDs) as meaningful error messages.
- **FR-007**: Tools MUST reuse the existing service and schema
  classes without duplicating scraping or parsing logic.

### Key Entities

- **Tool**: An ADK FunctionTool wrapping one scraping service. Has a
  name, description, input parameters, and JSON output.
- **Service**: Existing `TransfermarktBase` subclass that fetches
  and parses a Transfermarkt page.
- **Schema**: Existing Pydantic model that defines the structured
  response for a given service.

### Tools Inventory

**Players** (8 tools):

| Tool | Service Class | Parameters |
|------|---------------|------------|
| get_player_profile | TransfermarktPlayerProfile | player_id |
| get_player_market_value | TransfermarktPlayerMarketValue | player_id |
| get_player_transfers | TransfermarktPlayerTransfers | player_id |
| get_player_stats | TransfermarktPlayerStats | player_id |
| get_player_injuries | TransfermarktPlayerInjuries | player_id, page_number? |
| get_player_jersey_numbers | TransfermarktPlayerJerseyNumbers | player_id |
| get_player_achievements | TransfermarktPlayerAchievements | player_id |
| search_players | TransfermarktPlayerSearch | query, page_number? |

**Clubs** (3 tools):

| Tool | Service Class | Parameters |
|------|---------------|------------|
| get_club_profile | TransfermarktClubProfile | club_id |
| get_club_players | TransfermarktClubPlayers | club_id, season_id? |
| search_clubs | TransfermarktClubSearch | query, page_number? |

**Competitions** (2 tools):

| Tool | Service Class | Parameters |
|------|---------------|------------|
| get_competition_clubs | TransfermarktCompetitionClubs | competition_id, season_id? |
| search_competitions | TransfermarktCompetitionSearch | query, page_number? |

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All 13 tools are individually invocable and return
  valid JSON matching the existing response schemas.
- **SC-002**: An ADK agent can list and discover all 13 tools
  with their names, descriptions, and parameter definitions.
- **SC-003**: Tools handle invalid input (unknown IDs, empty
  queries) by returning descriptive error messages rather than
  unhandled exceptions.
- **SC-004**: No existing API endpoint or service behavior is
  modified — tools are a new parallel interface to the same logic.

## Assumptions

- Google ADK (`google-adk`) is available as a Python dependency
  and will be added to the project via Poetry.
- The ADK `FunctionTool` (or equivalent) accepts plain Python
  functions with type annotations and docstrings for tool discovery.
- Tools do not need authentication or authorization — they mirror
  the existing public API.
- Tools are not exposed as HTTP endpoints — they are in-process
  callables for ADK agent consumption.
- The existing service classes remain unchanged; tools wrap them.
