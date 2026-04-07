"""ADK tool functions for Transfermarkt club data."""

from fastapi import HTTPException

from app.services.clubs.players import TransfermarktClubPlayers
from app.services.clubs.profile import TransfermarktClubProfile
from app.services.clubs.search import TransfermarktClubSearch


def get_club_profile(club_id: str) -> dict:
    """Get the full profile of a football club by its Transfermarkt ID."""
    try:
        tfmkt = TransfermarktClubProfile(club_id=club_id)
        return tfmkt.get_club_profile()
    except HTTPException as e:
        return {"error": f"Club not found (ID: {club_id}): {e.detail}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}


def get_club_players(club_id: str, season_id: str = None) -> dict:
    """Get the squad/player list of a football club, optionally for a specific season."""
    try:
        tfmkt = TransfermarktClubPlayers(club_id=club_id, season_id=season_id)
        return tfmkt.get_club_players()
    except HTTPException as e:
        return {"error": f"Club not found (ID: {club_id}): {e.detail}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}


def search_clubs(query: str, page_number: int = 1) -> dict:
    """Search for football clubs by name on Transfermarkt."""
    try:
        tfmkt = TransfermarktClubSearch(query=query, page_number=page_number)
        return tfmkt.search_clubs()
    except HTTPException as e:
        return {"error": f"Search failed: {e.detail}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}
