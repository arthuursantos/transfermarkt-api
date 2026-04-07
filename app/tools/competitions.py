"""ADK tool functions for Transfermarkt competition data."""

from fastapi import HTTPException

from app.services.competitions.clubs import TransfermarktCompetitionClubs
from app.services.competitions.search import TransfermarktCompetitionSearch


def get_competition_clubs(competition_id: str, season_id: str = None) -> dict:
    """Get the clubs participating in a football competition, optionally for a specific season."""
    try:
        tfmkt = TransfermarktCompetitionClubs(competition_id=competition_id, season_id=season_id)
        return tfmkt.get_competition_clubs()
    except HTTPException as e:
        return {"error": f"Competition not found (ID: {competition_id}): {e.detail}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}


def search_competitions(query: str, page_number: int = 1) -> dict:
    """Search for football competitions by name on Transfermarkt."""
    try:
        tfmkt = TransfermarktCompetitionSearch(query=query, page_number=page_number)
        return tfmkt.search_competitions()
    except HTTPException as e:
        return {"error": f"Search failed: {e.detail}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}
