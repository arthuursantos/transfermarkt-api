from datetime import datetime

from schema import And, Schema

from app.tools.competitions import get_competition_clubs, search_competitions


def test_search_competitions(len_greater_than_0):
    result = search_competitions(query="Premier League")

    expected_schema = Schema(
        {
            "query": "Premier League",
            "pageNumber": 1,
            "lastPageNumber": And(int, lambda x: x >= 1),
            "results": And(list, len_greater_than_0),
            "updatedAt": datetime,
        },
    )

    assert expected_schema.validate(result)


def test_get_competition_clubs(len_greater_than_0):
    result = get_competition_clubs(competition_id="GB1")

    assert isinstance(result, dict)
    assert "id" in result
    assert result["id"] == "GB1"
    assert "clubs" in result
    assert isinstance(result["clubs"], list)
    assert len(result["clubs"]) > 0


def test_get_competition_clubs_error():
    result = get_competition_clubs(competition_id="INVALID_ID_999")

    assert isinstance(result, dict)
    assert "error" in result
