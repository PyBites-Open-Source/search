import typer

from .article import ArticleSearch
from .bite import BiteSearch
from .youtube import YouTubeSearch

app = typer.Typer()


@app.command()
def article(search: str):
    searcher = ArticleSearch()
    results = searcher.match_content(search)
    searcher.show_matches(results)


@app.command()
def video(search: str):
    searcher = YouTubeSearch()
    results = searcher.match_content(search)
    searcher.show_matches(results)


@app.command()
def bite(search: str):
    searcher = BiteSearch()
    results = searcher.match_content(search)
    searcher.show_matches(results)
