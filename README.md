# Pybites Search

A command line tool to easily search across Pybites content.

## Installation

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

$ search all decouple
Pybites Articles
No results found

Pybites Bite Exercises
No results found

Pybites Podcast Episodes
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Title                                                   ┃ Url                                                                                               ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ #025 - Building Dreams with Python - The AskAGuru Story │ https://www.pybitespodcast.com/1501156/8476666-025-building-dreams-with-python-the-askaguru-story │
└─────────────────────────────────────────────────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────┘

Pybites Python Tips
┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Title                   ┃ Url                                                  ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ configuration variables │ https://codechalleng.es/tips/configuration-variables │
└─────────────────────────┴──────────────────────────────────────────────────────┘

Pybites YouTube videos
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Title                                                              ┃ Url                                         ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ How to manage environment variables in Django with python-decouple │ https://www.youtube.com/watch?v=LkyhTqDrSxA │
└────────────────────────────────────────────────────────────────────┴─────────────────────────────────────────────┘
```

## Caching

By default any requests calls to the different Pybites API endpoints are cached for 24 hours, you can change that setting the `CACHE_EXPIRATION_SECONDS` environment variable.

## Changelog

Check out the changelog [here](CHANGELOG.md)
