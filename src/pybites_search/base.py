from abc import ABCMeta, abstractmethod
from typing import NamedTuple

import requests
import requests_cache
from decouple import config
from rich.console import Console
from rich.table import Table
from rich.text import Text

ONE_DAY_IN_SECONDS = 24 * 60 * 60
CACHE_EXPIRATION_SECONDS = config(
    "CACHE_EXPIRATION_SECONDS", default=ONE_DAY_IN_SECONDS
)
TIMEOUT = 5

console = Console()
error_console = Console(stderr=True, style="bold red")

requests_cache.install_cache("search_cache", expire_after=CACHE_EXPIRATION_SECONDS)


class ContentPiece(NamedTuple):
    title: str
    url: str


class PybitesSearch(metaclass=ABCMeta):
    @abstractmethod
    def match_content(self, search: str) -> list[ContentPiece]:
        """Search through Pybites content, implement for a specific source"""

    def get_data(self, endpoint):
        return requests.get(endpoint, timeout=TIMEOUT).json()

    def show_header(self, title: str) -> None:
        header = Text(title, style="bold underline")
        console.print(header)

    def show_matches(self, content: list[ContentPiece], extra_nl: bool = False) -> None:
        """Show search results in a nice table"""
        if content:
            table = Table("Title", "Url")
            for row in content:
                table.add_row(row.title, row.url)
            console.print(table)
        else:
            error_console.print("No results found")

        if extra_nl:
            console.print()
