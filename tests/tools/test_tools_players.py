from datetime import datetime

from schema import And, Schema

from app.tools import ALL_TOOLS
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


def test_get_player_profile(len_greater_than_0):
    result = get_player_profile(player_id="28003")

    expected_schema = Schema(
        {
            "id": And(str, len_greater_than_0),
            "url": And(str, len_greater_than_0),
            "name": And(str, len_greater_than_0),
            "description": And(str, len_greater_than_0),
            "nameInHomeCountry": And(str, len_greater_than_0),
            "imageURL": And(str, len_greater_than_0),
            "dateOfBirth": And(str, len_greater_than_0),
            "placeOfBirth": {
                "city": And(str, len_greater_than_0),
                "country": And(str, len_greater_than_0),
            },
            "age": And(str, len_greater_than_0),
            "height": And(str, len_greater_than_0),
            "citizenship": And(list, len_greater_than_0),
            "isRetired": bool,
            "position": {
                "main": And(str, len_greater_than_0),
                "other": And(list, len_greater_than_0),
            },
            "foot": And(str, len_greater_than_0),
            "shirtNumber": And(str, len_greater_than_0),
            "club": {
                "id": And(str, len_greater_than_0),
                "name": And(str, len_greater_than_0),
                "joined": And(str, len_greater_than_0),
                "contractExpires": And(str, len_greater_than_0),
            },
            "marketValue": And(str, len_greater_than_0),
            "agent": {
                "name": And(str, len_greater_than_0),
            },
            "outfitter": And(str, len_greater_than_0),
            "socialMedia": And(list, len_greater_than_0),
            "relatives": [
                {
                    "id": And(str, len_greater_than_0),
                    "url": And(str, len_greater_than_0),
                    "name": And(str, len_greater_than_0),
                    "profileType": And(str, len_greater_than_0),
                },
            ],
            "updatedAt": datetime,
        },
    )

    assert expected_schema.validate(result)


def test_get_player_market_value(len_greater_than_0):
    result = get_player_market_value(player_id="28003")

    assert isinstance(result, dict)
    assert "id" in result
    assert result["id"] == "28003"
    assert "marketValue" in result or "currentMarketValue" in result or "marketValueHistory" in result


def test_get_player_transfers(len_greater_than_0):
    result = get_player_transfers(player_id="28003")

    assert isinstance(result, dict)
    assert "id" in result
    assert result["id"] == "28003"
    assert "transfers" in result
    assert isinstance(result["transfers"], list)


def test_get_player_stats(len_greater_than_0):
    result = get_player_stats(player_id="28003")

    assert isinstance(result, dict)
    assert "id" in result
    assert result["id"] == "28003"


def test_get_player_injuries(len_greater_than_0):
    result = get_player_injuries(player_id="28003")

    assert isinstance(result, dict)
    assert "id" in result
    assert result["id"] == "28003"
    assert "injuries" in result
    assert isinstance(result["injuries"], list)


def test_get_player_jersey_numbers(len_greater_than_0):
    result = get_player_jersey_numbers(player_id="28003")

    assert isinstance(result, dict)
    assert "id" in result
    assert result["id"] == "28003"
    assert "jerseyNumbers" in result
    assert isinstance(result["jerseyNumbers"], list)


def test_get_player_achievements(len_greater_than_0):
    result = get_player_achievements(player_id="28003")

    assert isinstance(result, dict)
    assert "id" in result
    assert result["id"] == "28003"
    assert "achievements" in result
    assert isinstance(result["achievements"], list)


def test_search_players(len_greater_than_0):
    result = search_players(query="Messi")

    expected_schema = Schema(
        {
            "query": "Messi",
            "pageNumber": 1,
            "lastPageNumber": And(int, lambda x: x >= 1),
            "results": And(list, len_greater_than_0),
            "updatedAt": datetime,
        },
    )

    assert expected_schema.validate(result)


def test_get_player_profile_error():
    result = get_player_profile(player_id="0")

    assert isinstance(result, dict)
    assert "error" in result


def test_all_tools_count():
    assert len(ALL_TOOLS) == 13


def test_all_tools_have_docstrings():
    for tool in ALL_TOOLS:
        assert tool.__doc__ is not None and len(tool.__doc__.strip()) > 0, f"{tool.__name__} missing docstring"
