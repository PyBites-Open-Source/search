from abc import ABCMeta, abstractmethod
from typing import NamedTuple

from rich.console import Console
from rich.table import Table

console = Console()
error_console = Console(stderr=True, style="bold red")


class ContentPiece(NamedTuple):
    title: str
    url: str


class PybitesSearch(metaclass=ABCMeta):
    @abstractmethod
    def match_content(self, search: str) -> list[ContentPiece]:
        """Search through Pybites content, implement for a specific source"""

    def show_matches(self, content: list[ContentPiece]) -> None:
        """Show search results in a nice table"""
        if content:
            table = Table("Title", "Url")
            for row in content:
                table.add_row(row.title, row.url)
            console.print(table)
        else:
            error_console.print("No results found")
