import json
from unittest.mock import patch

import requests

from pybites_search.podcast import ContentPiece, PodcastSearch


def test_match_podcast_content():
    with open("tests/data/podcast.json") as f:
        json_data = json.loads(f.read())

    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = json.dumps(json_data).encode()

    with patch("requests.get", return_value=mock_response):
        searcher = PodcastSearch()
        results = searcher.match_content("packaging")

    expected_results = [
        ContentPiece(
            title="#110 - Dane Hillard on Python packaging and effective developer tooling",
            url="https://www.pybitespodcast.com/1501156/12592983-110-dane-hillard-on-python-packaging-and-effective-developer-tooling",
        ),
        ContentPiece(
            title="#108 - Teaching packaging by building a Python package",
            url="https://www.pybitespodcast.com/1501156/12512231-108-teaching-packaging-by-building-a-python-package",
        ),
    ]
    assert results == expected_results
