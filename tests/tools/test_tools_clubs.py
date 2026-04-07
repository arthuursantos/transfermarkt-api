from datetime import datetime

from schema import And, Schema

from app.tools.clubs import get_club_players, get_club_profile, search_clubs


def test_get_club_profile(len_greater_than_0):
    result = get_club_profile(club_id="131")

    assert isinstance(result, dict)
    assert "id" in result
    assert result["id"] == "131"
    assert "name" in result
    assert isinstance(result["name"], str)


def test_get_club_players(len_greater_than_0):
    result = get_club_players(club_id="131")

    assert isinstance(result, dict)
    assert "id" in result
    assert result["id"] == "131"
    assert "players" in result
    assert isinstance(result["players"], list)
    assert len(result["players"]) > 0


def test_search_clubs(len_greater_than_0):
    result = search_clubs(query="Barcelona")

    expected_schema = Schema(
        {
            "query": "Barcelona",
            "pageNumber": 1,
            "lastPageNumber": And(int, lambda x: x >= 1),
            "results": And(list, len_greater_than_0),
            "updatedAt": datetime,
        },
    )

    assert expected_schema.validate(result)


def test_get_club_profile_error():
    result = get_club_profile(club_id="0")

    assert isinstance(result, dict)
    assert "error" in result
