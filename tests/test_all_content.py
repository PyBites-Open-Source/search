from unittest.mock import patch

from pybites_search.all_content import AllSearch, ContentPiece


class MockResponse:
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data


def test_all_search_match_content():
    mock_responses = [
        # articles
        [
            {
                "title": "Django vs Flask: Which Framework to Choose?",
                "summary": "Comparing the two most popular Python web frameworks",
                "link": "https://example.com/django-vs-flask",
            }
        ],
        # bites
        [
            {
                "title": "Bite 1: Hello, World!",
                "description": "Write a program that prints 'Hello, World!'",
                "number": 1,
            },
        ],
        # podcasts
        [
            {
                "slug": "some-slug",
                "title": "#80 - fastapi episode",
                "description": "some description",
                "publish_date": "2022-04-05 11:00:00+00:00",
            }
        ],
        # tips
        [
            {
                "title": "Zen of Python",
                "description": 'What is #Python\'s philosophy? Run "import this" in the REPL',
                "link": "https://codechalleng.es/tips/zen-of-python",
            },
            {
                "title": "braces?",
                "description": "Will #Python ever support braces?",
                "link": "https://codechalleng.es/tips/braces",
            },
        ],
        # yt videos
        [
            {
                "title": "FastAPI Basics",
                "description": "Learn the basics of FastAPI",
                "video_id": "abc123",
            }
        ],
    ]
    with patch("requests.get") as mock_get:
        mock_get.side_effect = [MockResponse(data) for data in mock_responses]
        searcher = AllSearch()
        results = searcher.match_content("fastapi")
        expected = [
            ContentPiece(
                title="#80 - fastapi episode",
                url="https://www.pybitespodcast.com/1501156/some-slug",
                channel="Pybites Podcast Episodes",
            ),
            ContentPiece(
                title="FastAPI Basics",
                url="https://www.youtube.com/watch?v=abc123",
                channel="Pybites YouTube Videos",
            ),
        ]
        assert results == expected


def test_all_search_show_matches(capfd):
    content = [
        ContentPiece(
            title="FastAPI Tutorial",
            url="https://example.com/fastapi",
            channel="Article",
        ),
        ContentPiece(
            title="FastAPI: A Modern Web Framework",
            url="https://example.com/fastapi2",
            channel="Article",
        ),
        ContentPiece(
            title="Python Bytes Podcast #235: FastAPI",
            url="https://example.com/fastapi3",
            channel="Podcast",
        ),
    ]

    expected_output_text = []
    for content_piece in content:
        expected_output_text.append(content_piece.title)
        expected_output_text.append(content_piece.url)

    with patch("pybites_search.base.console"):
        searcher = AllSearch()
        searcher.show_matches(content)
        captured = capfd.readouterr()[0]
        for text in expected_output_text:
            assert text in captured
