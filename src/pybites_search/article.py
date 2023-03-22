import requests

from .base import ContentPiece, PybitesSearch

ARTICLE_ENDPOINT = "https://codechalleng.es/api/articles/"


class ArticleSearch(PybitesSearch):
    def match_content(self, search: str) -> list[ContentPiece]:
        entries = requests.get(ARTICLE_ENDPOINT, timeout=5).json()
        results = []
        for entry in entries:
            if search.lower() in (entry["title"] + entry["summary"]).lower():
                results.append(
                    ContentPiece(
                        title=entry["title"],
                        url=entry["link"],
                    )
                )
        return results


if __name__ == "__main__":
    searcher = ArticleSearch()
    results = searcher.match_content("django")
    searcher.show_matches(results)
