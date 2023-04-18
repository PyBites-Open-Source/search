from unittest.mock import MagicMock, patch

import requests

from pybites_search.youtube import YouTubeSearch


def test_match_video_content():
    mock_response = MagicMock()
    mock_response.json.return_value = [
        {
            "title": "Django Basics",
            "description": "Learn the basics of Django",
            "video_id": "abc123",
        },
        {
            "title": "Flask vs Django",
            "description": "A comparison of Flask and Django",
            "video_id": "def456",
        },
        {
            "title": "Django vs Rails",
            "description": "A comparison of Django and Rails",
            "video_id": "ghi789",
        },
    ]
    with patch.object(requests, "get", return_value=mock_response):
        searcher = YouTubeSearch()

        # all results have django
        results = searcher.match_content("Django")
        assert len(results) == 3
        assert results[0].title == "Django Basics"
        assert results[0].url == "https://www.youtube.com/watch?v=abc123"
        assert results[1].title == "Flask vs Django"
        assert results[1].url == "https://www.youtube.com/watch?v=def456"
        assert results[2].title == "Django vs Rails"
        assert results[2].url == "https://www.youtube.com/watch?v=ghi789"

        # searches description as well
        results = searcher.match_content("comparison")
        assert len(results) == 2

        # search is case insensitive
        results = searcher.match_content("flask")
        assert len(results) == 1

        # python is not in there
        results = searcher.match_content("python")
        assert len(results) == 0
