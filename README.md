# Pybites Search

A command line tool to easily search across Pybites content.

**Update April 2026**: the Pybites v1 Platform (codechalleng.es) and this tool are EOL. 
You can still use the [Rust version](https://crates.io/crates/pybites-search) to search legacy Pybites content.

## Installation

`pybites-search` is hosted on PyPI and you can install it in a virtual environment like this:

```
$ pip install pybites-search
```

## How to run it:

```
$ search --help

 Usage: search [OPTIONS] COMMAND [ARGS]...

╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                                                     │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                                              │
│ --help                        Show this message and exit.                                                                                                   │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ all                                                                                                                                                         │
│ article                                                                                                                                                     │
│ bite                                                                                                                                                        │
│ podcast                                                                                                                                                     │
│ tip                                                                                                                                                         │
│ video                                                                                                                                                       │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

$ search article zipfiles
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Title                                        ┃ Url                                   ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ How to Create and Serve Zipfiles from Django │ https://pybit.es/django-zipfiles.html │
└──────────────────────────────────────────────┴───────────────────────────────────────┘

$ search bite fastapi
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Title                                             ┃ Url                               ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ FastAPI Exception handling                        │ https://codechalleng.es/bites/343 │
│ FastAPI Hello World                               │ https://codechalleng.es/bites/336 │
│ A little detour: Pydantic                         │ https://codechalleng.es/bites/337 │
│ Update and delete food objects                    │ https://codechalleng.es/bites/340 │
│ Food logging CRUD                                 │ https://codechalleng.es/bites/342 │
│ FastAPI Authentication with JWT (JSON Web Tokens) │ https://codechalleng.es/bites/345 │
│ Return an HTML response                           │ https://codechalleng.es/bites/344 │
│ Create food objects                               │ https://codechalleng.es/bites/338 │
│ Retrieve food objects                             │ https://codechalleng.es/bites/339 │
│ Pydantic part II                                  │ https://codechalleng.es/bites/341 │
└───────────────────────────────────────────────────┴───────────────────────────────────┘

$ search podcast layoff
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Title                                          ┃ Url                                                                                        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ #101 - Layoff fears, 5 tips to stay in control │ https://www.buzzsprout.com/1501156/12125495-101-layoff-fears-5-tips-to-stay-in-control.mp3 │
└────────────────────────────────────────────────┴────────────────────────────────────────────────────────────────────────────────────────────┘

$ search tip unpacking
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Title                              ┃ Url                                                             ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ tuple unpacking                    │ https://codechalleng.es/tips/tuple-unpacking                    │
│ regex replace                      │ https://codechalleng.es/tips/regex-replace                      │
│ dictionary unpacking               │ https://codechalleng.es/tips/dictionary-unpacking               │
│ extract dictionary keys and values │ https://codechalleng.es/tips/extract-dictionary-keys-and-values │
│ dataclass from dict                │ https://codechalleng.es/tips/dataclass-from-dict                │
└────────────────────────────────────┴─────────────────────────────────────────────────────────────────┘

$ search video property
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Title                                ┃ Url                                         ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Python @property decorator explained │ https://www.youtube.com/watch?v=8BbngXWouzo │
└──────────────────────────────────────┴─────────────────────────────────────────────┘

# and to search across all content channels:

$ search all decouple
                                                                           Pybites All Content
┌────────────────────────────────────────────────────────────────────┬───────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Pybites Podcast Episodes                                           │ Url                                                                                               │
├────────────────────────────────────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
│ #025 - Building Dreams with Python - The AskAGuru Story            │ https://www.pybitespodcast.com/1501156/8476666-025-building-dreams-with-python-the-askaguru-story │
├────────────────────────────────────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Pybites Python Tips                                                │ Url                                                                                               │
├────────────────────────────────────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
│ configuration variables                                            │ https://codechalleng.es/tips/configuration-variables                                              │
├────────────────────────────────────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Pybites YouTube Videos                                             │ Url                                                                                               │
├────────────────────────────────────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
│ How to manage environment variables in Django with python-decouple │ https://www.youtube.com/watch?v=LkyhTqDrSxA                                                       │
└────────────────────────────────────────────────────────────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Caching

By default any requests calls to the different Pybites API endpoints are cached for 24 hours, you can change that setting the `CACHE_EXPIRATION_SECONDS` environment variable.

## Changelog

Check out the changelog [here](CHANGELOG.md)

## Developer setup instructions

We recommend using [uv](https://pypi.org/project/uv/) for development work on this repo. (Preferably installed via one of the standalone installers)

1. Check out the repo.

```
# original repo or make a fork and clone that if you want to contribute

$ git clone git@github.com:PyBites-Open-Source/search.git
```

2. Activate the virtual environment  
*(This is optional if you run **all your commands** with `uv`, but is a safer option if you are new to this workflow)*
```
# Linux and macOS
√ search (main) $ source venv/bin/activate

# Windows
√ search (main) $ .venv\scripts\activate
```

3. Install dependencies (this will automatically include the *dev* dependency group)

```
(search) √ search (main) $ uv sync
```

4. Use the tool / run the tests

```
(search) √ search (main) $ search ...
...

(search) √ search (main) $ uv run pytest -vvv
...
...
configfile: pyproject.toml
plugins: cov-6.2.1
collected 11 items

tests/test_all_content.py::test_all_search_match_content PASSED          [  9%]
tests/test_all_content.py::test_all_search_show_matches PASSED           [ 18%]
tests/test_article.py::test_match_article_content PASSED                 [ 27%]
tests/test_article.py::test_match_article_content_no_results PASSED      [ 36%]
tests/test_bite.py::test_match_bite_content PASSED                       [ 45%]
tests/test_bite.py::test_match_bite_content_no_results PASSED            [ 54%]
tests/test_bite.py::test_match_bite_content_timeout PASSED               [ 63%]
tests/test_podcast.py::test_match_podcast_content PASSED                 [ 72%]
tests/test_tip.py::test_match_tip_content PASSED                         [ 81%]
tests/test_tip.py::test_show_tip_matches PASSED                          [ 90%]
tests/test_youtube.py::test_match_video_content PASSED                   [100%]

============================= 11 passed in 0.34s ==============================

6. Code, have fun, contribute ... 💪 🙏
