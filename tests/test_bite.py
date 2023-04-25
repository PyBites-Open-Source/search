from unittest.mock import patch

import pytest
import requests

from pybites_search.bite import BiteSearch, ContentPiece

CHANNEL = "Pybites Bite Exercises"


def test_match_bite_content():
    mock_entries = [
        {
            "title": "Bite 1: Hello, World!",
            "description": "Write a program that prints 'Hello, World!'",
            "number": 1,
        },
        {
            "title": "Bite 2: String Formatting",
            "description": "Learn the basics of string formatting in Python",
            "number": 2,
        },
        {
            "title": "Bite 3: Palindromes",
            "description": "Write a function to check if a word is a palindrome",
            "number": 3,
        },
    ]
    mock_response = requests.models.Response()
    mock_response.json = lambda: mock_entries
    with patch("requests.get", return_value=mock_response):
        searcher = BiteSearch()
        results = searcher.match_content("palindrome")

    expected_results = [
        ContentPiece(
            title="Bite 3: Palindromes",
            url="https://codechalleng.es/bites/3",
            channel=CHANNEL,
        ),
    ]
    assert results == expected_results


def test_match_bite_content_no_results():
    mock_entries = [
        {
            "title": "Bite 1: Hello, World!",
            "description": "Write a program that prints 'Hello, World!'",
            "number": 1,
        },
        {
            "title": "Bite 2: String Formatting",
            "description": "Learn the basics of string formatting in Python",
            "number": 2,
        },
        {
            "title": "Bite 3: Palindromes",
            "description": "Write a function to check if a word is a palindrome",
            "number": 3,
        },
    ]
    mock_response = requests.models.Response()
    mock_response.json = lambda: mock_entries
    with patch("requests.get", return_value=mock_response):
        searcher = BiteSearch()
        results = searcher.match_content("fastapi")

    assert results == []


def test_match_bite_content_timeout():
    with patch("requests.get", side_effect=requests.exceptions.Timeout):
        searcher = BiteSearch()
        with pytest.raises(requests.exceptions.Timeout):
            searcher.match_content("palindrome")
