import typer

from .all_content import AllSearch
from .article import ArticleSearch
from .bite import BiteSearch
from .podcast import PodcastSearch
from .tip import TipSearch
from .youtube import YouTubeSearch

app = typer.Typer()


def search_content(searcher, search):
    results = searcher.match_content(search)
    searcher.show_matches(results)


@app.command()
def article(search: str):
    search_content(ArticleSearch(), search)


@app.command()
def bite(search: str):
    search_content(BiteSearch(), search)


@app.command()
def podcast(search: str):
    search_content(PodcastSearch(), search)


@app.command()
def tip(search: str):
    search_content(TipSearch(), search)


@app.command()
def video(search: str):
    search_content(YouTubeSearch(), search)


@app.command()
def all(search: str):
    search_content(AllSearch(), search)
