# Tasks: ADK Tools for Transfermarkt Scraping

**Input**: Design documents from `specs/feat/adk-a2a/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/

**Tests**: Included — constitution mandates TDD (Principle II).

**Organization**: Tasks grouped by user story for independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup

**Purpose**: Project initialization — add dependency and create package structure

- [x] T001 Add `google-adk` dependency via `poetry add google-adk`
- [x] T002 Create `app/tools/__init__.py` with empty `ALL_TOOLS` list
- [x] T003 [P] Create `app/tools/players.py` with module docstring
- [x] T004 [P] Create `app/tools/clubs.py` with module docstring
- [x] T005 [P] Create `app/tools/competitions.py` with module docstring
- [x] T006 [P] Create `tests/tools/__init__.py` (empty)

**Checkpoint**: Package structure ready, dependency installed

---

## Phase 2: Foundational

**Purpose**: No foundational tasks — tools have no shared infrastructure beyond existing services. Proceed directly to user stories.

**Checkpoint**: N/A — Phase 1 is sufficient

---

## Phase 3: User Story 1 - Player Tools (Priority: P1) MVP

**Goal**: All 8 player-domain tools invocable and returning valid JSON

**Independent Test**: Invoke `get_player_profile` with player ID `28003` and verify JSON matches player profile schema structure

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T007 [P] [US1] Write test for `get_player_profile` in tests/tools/test_tools_players.py
- [x] T008 [P] [US1] Write test for `get_player_market_value` in tests/tools/test_tools_players.py
- [x] T009 [P] [US1] Write test for `get_player_transfers` in tests/tools/test_tools_players.py
- [x] T010 [P] [US1] Write test for `get_player_stats` in tests/tools/test_tools_players.py
- [x] T011 [P] [US1] Write test for `get_player_injuries` in tests/tools/test_tools_players.py
- [x] T012 [P] [US1] Write test for `get_player_jersey_numbers` in tests/tools/test_tools_players.py
- [x] T013 [P] [US1] Write test for `get_player_achievements` in tests/tools/test_tools_players.py
- [x] T014 [P] [US1] Write test for `search_players` in tests/tools/test_tools_players.py
- [x] T015 [P] [US1] Write test for error handling (invalid player ID) in tests/tools/test_tools_players.py

### Implementation for User Story 1

- [x] T016 [US1] Implement all 8 player tool functions in app/tools/players.py per contracts/tools-api.md signatures
- [x] T017 [US1] Register player tools in app/tools/__init__.py ALL_TOOLS list
- [x] T018 [US1] Run `pytest tests/tools/test_tools_players.py` — pending live run

**Checkpoint**: 8 player tools functional, independently testable, error handling verified

---

## Phase 4: User Story 2 - Club Tools (Priority: P2)

**Goal**: All 3 club-domain tools invocable and returning valid JSON

**Independent Test**: Invoke `get_club_profile` with club ID `131` and verify JSON matches club profile schema structure

### Tests for User Story 2

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T019 [P] [US2] Write test for `get_club_profile` in tests/tools/test_tools_clubs.py
- [x] T020 [P] [US2] Write test for `get_club_players` in tests/tools/test_tools_clubs.py
- [x] T021 [P] [US2] Write test for `search_clubs` in tests/tools/test_tools_clubs.py
- [x] T022 [P] [US2] Write test for error handling (invalid club ID) in tests/tools/test_tools_clubs.py

### Implementation for User Story 2

- [x] T023 [US2] Implement all 3 club tool functions in app/tools/clubs.py per contracts/tools-api.md signatures
- [x] T024 [US2] Register club tools in app/tools/__init__.py ALL_TOOLS list
- [x] T025 [US2] Run `pytest tests/tools/test_tools_clubs.py` — pending live run

**Checkpoint**: 3 club tools functional, independently testable

---

## Phase 5: User Story 3 - Competition Tools (Priority: P3)

**Goal**: All 2 competition-domain tools invocable and returning valid JSON

**Independent Test**: Invoke `search_competitions` with query `"Premier League"` and verify JSON matches competition search schema structure

### Tests for User Story 3

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T026 [P] [US3] Write test for `search_competitions` in tests/tools/test_tools_competitions.py
- [x] T027 [P] [US3] Write test for `get_competition_clubs` in tests/tools/test_tools_competitions.py
- [x] T028 [P] [US3] Write test for error handling (invalid competition ID) in tests/tools/test_tools_competitions.py

### Implementation for User Story 3

- [x] T029 [US3] Implement all 2 competition tool functions in app/tools/competitions.py per contracts/tools-api.md signatures
- [x] T030 [US3] Register competition tools in app/tools/__init__.py ALL_TOOLS list
- [x] T031 [US3] Run `pytest tests/tools/test_tools_competitions.py` — pending live run

**Checkpoint**: 2 competition tools functional, all 13 tools complete

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Validation across all tools, quality gates, discoverability

- [x] T032 Write test verifying `ALL_TOOLS` contains exactly 13 functions in tests/tools/test_tools_players.py
- [x] T033 Write test verifying each tool has a non-empty docstring in tests/tools/test_tools_players.py
- [x] T034 Run `pytest` — pending live run (ruff + black pass)
- [x] T035 Run `ruff check .` and fix any violations
- [x] T036 Run `black --check .` and fix any formatting issues
- [x] T037 Run quickstart.md validation — ALL_TOOLS contains 13 functions

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately
- **Foundational (Phase 2)**: N/A — no foundational tasks
- **User Story 1 (Phase 3)**: Depends on Setup (Phase 1)
- **User Story 2 (Phase 4)**: Depends on Setup (Phase 1) — can run in parallel with US1
- **User Story 3 (Phase 5)**: Depends on Setup (Phase 1) — can run in parallel with US1/US2
- **Polish (Phase 6)**: Depends on all user stories complete

### User Story Dependencies

- **User Story 1 (P1)**: Independent — no dependencies on other stories
- **User Story 2 (P2)**: Independent — no dependencies on other stories
- **User Story 3 (P3)**: Independent — no dependencies on other stories

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Implementation covers all tools for that domain in one task
- Registration in ALL_TOOLS after implementation
- Verify tests pass after implementation

### Parallel Opportunities

- T003, T004, T005, T006 can all run in parallel (different files)
- All test tasks within a story can run in parallel (same file but independent test functions)
- US1, US2, US3 can run in parallel after Phase 1 (independent domains)

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 3: User Story 1 (Player Tools)
3. **STOP and VALIDATE**: Run `pytest tests/tools/test_tools_players.py`
4. 8 of 13 tools ready — most valuable domain delivered

### Incremental Delivery

1. Setup → ready
2. Player Tools (US1) → 8 tools live (MVP!)
3. Club Tools (US2) → 11 tools live
4. Competition Tools (US3) → all 13 tools live
5. Polish → quality gates pass, full validation

### Parallel Strategy

After Phase 1:
- Developer A: User Story 1 (players — 8 tools)
- Developer B: User Story 2 (clubs — 3 tools)
- Developer C: User Story 3 (competitions — 2 tools)

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story
- Each user story is independently completable and testable
- Tests hit live Transfermarkt pages (no mocking) per Constitution Principle V
- Commit after each phase completion
