from unittest.mock import patch

import requests

from pybites_search.article import ArticleSearch, ContentPiece

CHANNEL = "Pybites Articles"


def test_match_article_content():
    mock_entries = [
        {
            "title": "Django vs Flask: Which Framework to Choose?",
            "summary": "Comparing the two most popular Python web frameworks",
            "link": "https://example.com/django-vs-flask",
        },
        {
            "title": "Building a CMS with Django",
            "summary": "A step-by-step guide to building a content management system with Django",
            "link": "https://example.com/django-cms",
        },
        {
            "title": "Flask for Beginners",
            "summary": "Learn Flask from the ground up",
            "link": "https://example.com/flask-beginners",
        },
    ]
    mock_response = requests.models.Response()
    mock_response.json = lambda: mock_entries
    with patch("requests.get", return_value=mock_response):
        searcher = ArticleSearch()
        results = searcher.match_content("django")

    expected_results = [
        ContentPiece(
            title="Django vs Flask: Which Framework to Choose?",
            url="https://example.com/django-vs-flask",
            channel=CHANNEL,
        ),
        ContentPiece(
            title="Building a CMS with Django",
            url="https://example.com/django-cms",
            channel=CHANNEL,
        ),
    ]
    assert results == expected_results


def test_match_article_content_no_results():
    mock_entries = [
        {
            "title": "Django vs Flask: Which Framework to Choose?",
            "summary": "Comparing the two most popular Python web frameworks",
            "link": "https://example.com/django-vs-flask",
        },
        {
            "title": "Building a CMS with Django",
            "summary": "A step-by-step guide to building a content management system with Django",
            "link": "https://example.com/django-cms",
        },
        {
            "title": "Flask for Beginners",
            "summary": "Learn Flask from the ground up",
            "link": "https://example.com/flask-beginners",
        },
    ]
    mock_response = requests.models.Response()
    mock_response.json = lambda: mock_entries
    with patch("requests.get", return_value=mock_response):
        searcher = ArticleSearch()
        results = searcher.match_content("fastapi")
    assert results == []
