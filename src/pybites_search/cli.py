import typer

from .article import ArticleSearch
from .bite import BiteSearch
from .podcast import PodcastSearch
from .tip import TipSearch
from .youtube import YouTubeSearch

app = typer.Typer()


@app.command()
def article(search: str):
    searcher = ArticleSearch()
    results = searcher.match_content(search)
    searcher.show_matches(results)


@app.command()
def bite(search: str):
    searcher = BiteSearch()
    results = searcher.match_content(search)
    searcher.show_matches(results)


@app.command()
def podcast(search: str):
    searcher = PodcastSearch()
    results = searcher.match_content(search)
    searcher.show_matches(results)


@app.command()
def tip(search: str):
    searcher = TipSearch()
    results = searcher.match_content(search)
    searcher.show_matches(results)


@app.command()
def video(search: str):
    searcher = YouTubeSearch()
    results = searcher.match_content(search)
    searcher.show_matches(results)


@app.command()
def all(search: str):
    classes = (ArticleSearch, BiteSearch, PodcastSearch, TipSearch, YouTubeSearch)
    titles = (
        "Articles",
        "Bite Exercises",
        "Podcast Episodes",
        "Python Tips",
        "YouTube videos",
    )
    for title, cls_ in zip(titles, classes):
        searcher = cls_()  # type: ignore
        results = searcher.match_content(search)
        title = f"Pybites {title}"
        searcher.show_header(title)
        searcher.show_matches(results, extra_nl=True)
