from rich.table import Table

from .article import ArticleSearch
from .base import STYLE_HEADER, ContentPiece, PybitesSearch, console, error_console
from .bite import BiteSearch
from .podcast import PodcastSearch
from .tip import TipSearch
from .youtube import YouTubeSearch


class AllSearch(PybitesSearch):
    def __init__(self) -> None:
        self.title = "Pybites All Content"

    def match_content(self, search: str) -> list[ContentPiece]:
        classes = (ArticleSearch, BiteSearch, PodcastSearch, TipSearch, YouTubeSearch)
        results = []
        for cls_ in classes:
            searcher = cls_()
            results.extend(searcher.match_content(search))

        return results

    def show_matches(self, content: list[ContentPiece]) -> None:
        """Show search results in a nice table"""
        if content:
            channel = None
            table = Table(
                "Title",
                "Url",
                title=self.title,
                header_style=STYLE_HEADER,
                show_header=False,
                title_style=STYLE_HEADER,
            )
            for row in content:
                if row.channel != channel:
                    if channel:
                        table.add_section()
                    table.add_row(
                        row.channel,
                        "Url",
                        style=STYLE_HEADER,
                        end_section=True,
                    )
                    channel = row.channel
                table.add_row(row.title, row.url)

            console.print(table)
        else:
            error_console.print("No results found")


if __name__ == "__main__":
    searcher = AllSearch()
    results = searcher.match_content("fastapi")
    searcher.show_matches(results)
