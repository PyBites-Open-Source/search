import requests

from .base import PybitesSearch, ContentPiece

ARTICLE_ENDPOINT = "https://codechalleng.es/api/articles/"


class ArticleSearch(PybitesSearch):

    def match_content(self, search: str) -> list[ContentPiece]:
        entries = requests.get(ARTICLE_ENDPOINT).json()
        results = []
        for entry in entries:
            if search.lower() in (
                entry["title"] + entry["summary"]
            ).lower():
                results.append(
                    ContentPiece(
                        title=entry["title"],
                        url=entry["link"],
                    )
                )
        return results


if __name__ == "__main__":
    search = ArticleSearch()
    results = search.match_content("django")
    print(results)
