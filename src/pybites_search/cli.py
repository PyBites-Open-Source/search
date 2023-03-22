import typer
from rich.console import Console
from rich.table import Table

from .article import ArticleSearch

console = Console()
app = typer.Typer()


@app.command()
def article(search: str):
    table = Table("Title", "URL")
    searcher = ArticleSearch()
    results = searcher.match_content(search)
    for row in results:
        table.add_row(row.title, row.url)
    console.print(table)
