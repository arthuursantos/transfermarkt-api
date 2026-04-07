"""ADK tool functions for Transfermarkt player data."""

from fastapi import HTTPException

from app.services.players.achievements import TransfermarktPlayerAchievements
from app.services.players.injuries import TransfermarktPlayerInjuries
from app.services.players.jersey_numbers import TransfermarktPlayerJerseyNumbers
from app.services.players.market_value import TransfermarktPlayerMarketValue
from app.services.players.profile import TransfermarktPlayerProfile
from app.services.players.search import TransfermarktPlayerSearch
from app.services.players.stats import TransfermarktPlayerStats
from app.services.players.transfers import TransfermarktPlayerTransfers


def get_player_profile(player_id: str) -> dict:
    """Get the full profile of a football player by their Transfermarkt ID."""
    try:
        tfmkt = TransfermarktPlayerProfile(player_id=player_id)
        return tfmkt.get_player_profile()
    except HTTPException as e:
        return {"error": f"Player not found (ID: {player_id}): {e.detail}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}


def get_player_market_value(player_id: str) -> dict:
    """Get market value history of a football player."""
    try:
        tfmkt = TransfermarktPlayerMarketValue(player_id=player_id)
        return tfmkt.get_player_market_value()
    except HTTPException as e:
        return {"error": f"Player not found (ID: {player_id}): {e.detail}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}


def get_player_transfers(player_id: str) -> dict:
    """Get the transfer history of a football player."""
    try:
        tfmkt = TransfermarktPlayerTransfers(player_id=player_id)
        return tfmkt.get_player_transfers()
    except HTTPException as e:
        return {"error": f"Player not found (ID: {player_id}): {e.detail}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}


def get_player_stats(player_id: str) -> dict:
    """Get career statistics of a football player."""
    try:
        tfmkt = TransfermarktPlayerStats(player_id=player_id)
        return tfmkt.get_player_stats()
    except HTTPException as e:
        return {"error": f"Player not found (ID: {player_id}): {e.detail}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}


def get_player_injuries(player_id: str, page_number: int = 1) -> dict:
    """Get the injury history of a football player."""
    try:
        tfmkt = TransfermarktPlayerInjuries(player_id=player_id, page_number=page_number)
        return tfmkt.get_player_injuries()
    except HTTPException as e:
        return {"error": f"Player not found (ID: {player_id}): {e.detail}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}


def get_player_jersey_numbers(player_id: str) -> dict:
    """Get the jersey number history of a football player."""
    try:
        tfmkt = TransfermarktPlayerJerseyNumbers(player_id=player_id)
        return tfmkt.get_player_jersey_numbers()
    except HTTPException as e:
        return {"error": f"Player not found (ID: {player_id}): {e.detail}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}


def get_player_achievements(player_id: str) -> dict:
    """Get the achievements and titles of a football player."""
    try:
        tfmkt = TransfermarktPlayerAchievements(player_id=player_id)
        return tfmkt.get_player_achievements()
    except HTTPException as e:
        return {"error": f"Player not found (ID: {player_id}): {e.detail}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}


def search_players(query: str, page_number: int = 1) -> dict:
    """Search for football players by name on Transfermarkt."""
    try:
        tfmkt = TransfermarktPlayerSearch(query=query, page_number=page_number)
        return tfmkt.search_players()
    except HTTPException as e:
        return {"error": f"Search failed: {e.detail}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}
