from .base import V2_BASE_URL, ContentPiece, PybitesSearch

BITES_ENDPOINT = V2_BASE_URL + "api/bites/"
BITES_URL = V2_BASE_URL + "bites/"


class BiteSearch(PybitesSearch):
    def __init__(self) -> None:
        self.title = "Pybites Bite Exercises"

    def match_content(self, search: str) -> list[ContentPiece]:
        entries = self.get_data(BITES_ENDPOINT)
        results = []
        for entry in entries:
            if search.lower() in (entry["title"] + entry["description"]).lower():
                results.append(
                    ContentPiece(
                        title=entry["title"],
                        url=f"{BITES_URL}{entry['slug']}",
                        channel=self.title,
                    )
                )
        return results


if __name__ == "__main__":
    searcher = BiteSearch()
    results = searcher.match_content("fastapi")
    searcher.show_matches(results)
