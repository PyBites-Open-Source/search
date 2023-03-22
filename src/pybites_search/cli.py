import typer

from .article import ArticleSearch

app = typer.Typer()


@app.command()
def article(search: str):
    searcher = ArticleSearch()
    results = searcher.match_content(search)
    searcher.show_matches(results)
