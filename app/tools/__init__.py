from app.tools.clubs import get_club_players, get_club_profile, search_clubs
from app.tools.competitions import get_competition_clubs, search_competitions
from app.tools.players import (
    get_player_achievements,
    get_player_injuries,
    get_player_jersey_numbers,
    get_player_market_value,
    get_player_profile,
    get_player_stats,
    get_player_transfers,
    search_players,
)

ALL_TOOLS = [
    get_player_profile,
    get_player_market_value,
    get_player_transfers,
    get_player_stats,
    get_player_injuries,
    get_player_jersey_numbers,
    get_player_achievements,
    search_players,
    get_club_profile,
    get_club_players,
    search_clubs,
    get_competition_clubs,
    search_competitions,
]
