# Pybites Search

A command line tool to easily search across Pybites content.

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

To do dev work on this repo:

1. Check out the repo and make a virtual environment and activate it:

```
# original repo or make a fork and clone that if you want to contribute

$ git clone git@github.com:PyBites-Open-Source/search.git

$ cd search
√ search (main) $ python3 -m venv venv && source venv/bin/activate

# for Windows this would be something like:
py -3 -m venv venv && venv\scripts\activate
```

2. Install the regular + test + tooling dependencies:

```
(venv) √ search (main) $ python -m pip install .
(venv) √ search (main) $ python -m pip install ".[test,tools]"
```

3. Use the tool / run the tests

```
(venv) √ search (main) $ search ...
...

(venv) √ search (main) $ tox
...
...
  py39: OK (15.89=setup[14.49]+cmd[1.40] seconds)
  py310: OK (13.22=setup[11.80]+cmd[1.42] seconds)
  py311: OK (10.42=setup[9.41]+cmd[1.01] seconds)
  congratulations :) (39.61 seconds)
```

4. Code, have fun, contribute ... 💪 🙏
