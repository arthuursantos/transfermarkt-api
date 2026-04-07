<!--
  Sync Impact Report
  ==================
  Version change: 1.0.0 → 1.1.0
  Modified principles: N/A
  Added sections:
    - Spec Directory Convention (under Development Workflow)
  Removed sections: N/A
  Templates requiring updates:
    - .specify/templates/plan-template.md ⚠ pending
      (spec path references use old [###-feature-name] pattern)
    - .specify/templates/spec-template.md ⚠ pending
      (branch name placeholder uses old pattern)
    - .specify/templates/tasks-template.md ⚠ pending
      (input path references use old pattern)
  Follow-up TODOs:
    - Update spec-kit templates to use feat/<branch> path convention
-->

# Transfermarkt API Constitution

## Core Principles

### I. Spec-Driven Development (SDD)

Every feature MUST begin with a formal specification before any code
is written. Specifications are created using the spec-kit workflows
(`/speckit.specify`, `/speckit.plan`, `/speckit.tasks`).

- A feature spec (`spec.md`) MUST exist and be reviewed before
  implementation planning begins.
- An implementation plan (`plan.md`) MUST be produced from the spec
  before task breakdown.
- No production code MUST be written without a corresponding spec
  and plan.

**Rationale**: Specifications force upfront thinking, reduce rework,
and serve as living documentation of intent.

### II. Test-Driven Development (TDD)

All feature code MUST follow the TDD cycle: write tests first,
verify they fail, then implement until tests pass.

- Tests MUST be written and committed before the implementation
  they validate.
- The Red-Green-Refactor cycle MUST be strictly followed.
- Tests MUST validate response structure against known
  Transfermarkt entity IDs (no mocking of external pages).

**Rationale**: TDD ensures correctness from the start and prevents
regression. Combined with SDD, the flow is:
spec → tests → implementation.

### III. Three-Layer Architecture

Every feature MUST follow the Endpoint → Service → Schema pattern.

- **Endpoints** (`app/api/endpoints/`): Thin route handlers that
  delegate to a service instance. No business logic.
- **Services** (`app/services/`): Inherit from `TransfermarktBase`.
  Fetch, parse, and extract data via XPath. Each domain has its
  own subdirectory.
- **Schemas** (`app/schemas/`): Pydantic v2 models with field
  validators for type conversion. Use camelCase aliases and
  `AuditMixin`.

New code MUST NOT introduce additional architectural layers or
bypass this pattern.

**Rationale**: A consistent, predictable structure keeps the
codebase navigable and reduces onboarding friction.

### IV. Code Quality Gates

All code MUST pass the following automated gates before merge:

- `ruff check .` — linting (pyflakes, pycodestyle, isort,
  flake8-commas, flake8-quotes, fastapi rules)
- `black --check .` — formatting (120-char line length)
- `interrogate app/services -vv` — 100% docstring coverage on
  all service classes
- `pytest` — full test suite with coverage, exits on first failure

No PR MUST be merged with any gate failing.

**Rationale**: Automated quality gates prevent style drift and
catch defects early, without relying on manual review discipline.

### V. Live Data Testing

Tests MUST hit live Transfermarkt pages. Mocking of HTTP responses
is NOT permitted for integration tests.

- Tests validate response structure using the `schema` library.
- Test fixtures in `tests/conftest.py` provide reusable validators
  (regex matchers, length checks).
- Tests use known, stable player/club/competition IDs.

**Rationale**: Mocks can mask real-world parsing failures. Testing
against live pages ensures the scraping logic stays aligned with
the actual Transfermarkt HTML structure.

## Technical Constraints

- **Language**: Python 3.x
- **Framework**: FastAPI
- **Dependency Management**: Poetry
- **Deployment**: Fly.io (with optional rate limiting via slowapi)
- **HTML Parsing**: lxml with XPath selectors (centralized in
  `app/utils/xpath.py`)
- **Response Models**: Pydantic v2 with `response_model_exclude_none=True`
- **Line Length**: 120 characters (enforced by black and ruff)

## Development Workflow

### Spec Directory Convention

Spec artifacts MUST be stored under `specs/feat/<current-branch>/`.
The branch name used is the current git branch at the time of
spec creation (e.g. `feat/adk-a2a` → `specs/feat/adk-a2a/`).

- The create-new-feature script MUST NOT be used to create branches.
  The developer creates the feature branch manually before running
  spec-kit workflows.
- `/speckit.specify` MUST write `spec.md` into `specs/feat/<branch>/`.
- `/speckit.plan` MUST write `plan.md` into the same directory.
- `/speckit.tasks` MUST write `tasks.md` into the same directory.

### Workflow Steps

The canonical development flow for every feature is:

1. **Branch** — Create the feature branch (`feat/<name>`).
2. **Specify** — Create the feature spec using `/speckit.specify`.
   Review and refine with `/speckit.clarify` if needed.
3. **Plan** — Generate the implementation plan using `/speckit.plan`.
   Validate against the Constitution Check gate in the plan template.
4. **Tasks** — Break down work using `/speckit.tasks`.
5. **Test** — Write failing tests per the spec's acceptance scenarios.
6. **Implement** — Write production code until all tests pass.
7. **Refactor** — Clean up while keeping tests green.
8. **Quality Gates** — Run `ruff`, `black`, `interrogate`, `pytest`.
9. **Review & Merge** — PR with passing gates.

## Governance

- This constitution is the authoritative source for development
  principles. It supersedes informal conventions or ad-hoc decisions.
- Amendments MUST be documented with a version bump, rationale,
  and migration plan if principles are removed or redefined.
- Versioning follows semantic versioning:
  - **MAJOR**: Principle removal or incompatible redefinition.
  - **MINOR**: New principle or materially expanded guidance.
  - **PATCH**: Clarifications, wording, or typo fixes.
- All PRs and code reviews MUST verify compliance with these
  principles.
- Use `CLAUDE.md` for runtime development guidance specific to
  tooling and commands.

**Version**: 1.1.0 | **Ratified**: 2026-04-02 | **Last Amended**: 2026-04-02
