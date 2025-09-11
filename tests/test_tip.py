import json
from unittest.mock import patch

import pytest
import requests

from pybites_search.base import V2_BASE_URL
from pybites_search.tip import ContentPiece, TipSearch

CHANNEL = "Pybites Python Tips"
TIPS_URL = V2_BASE_URL + "tips/"


@pytest.fixture
def mock_data():
    with open("tests/data/tips.json") as f:
        return json.loads(f.read())


def test_match_tip_content(mock_data):
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = json.dumps(mock_data).encode()

    with patch("requests.get", return_value=mock_response):
        searcher = TipSearch()

        results = searcher.match_content("zen")
        expected = [
            ContentPiece(
                title="Zen of Python",
                url=f"{TIPS_URL}zen-of-python",
                channel=CHANNEL,
            )
        ]
        assert results == expected

        results = searcher.match_content(" a")
        expected = [
            ContentPiece(
                title="import antigravity",
                url=f"{TIPS_URL}import-antigravity",
                channel=CHANNEL,
            ),
            ContentPiece(
                title="for ... else",
                url=f"{TIPS_URL}for-else",
                channel=CHANNEL,
            ),
        ]
        assert results == expected


def test_show_tip_matches(mock_data, capfd):
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = json.dumps(mock_data).encode()
    expected_output_text = []

    with patch("requests.get", return_value=mock_response):
        searcher = TipSearch()
        search_term = " a"
        for tip in mock_data:
            if search_term in (tip["title"] + tip["description"]):
                expected_output_text.append(tip["title"])
                expected_output_text.append(tip["slug"])

        results = searcher.match_content(search_term)

        searcher.show_matches(results)
        output = capfd.readouterr()[0]
        for text in expected_output_text:
            assert text in output

        results = searcher.match_content("bogus")
        searcher.show_matches(results)
        err_output = capfd.readouterr()[1]
        assert err_output.strip() == "No results found"
