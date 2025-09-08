from .base import ContentPiece, PybitesSearch, V2_BASE_URL

TIPS_ENDPOINT = V2_BASE_URL + "api/tips/"
TIPS_URL = V2_BASE_URL + "tips/"


class TipSearch(PybitesSearch):
    def __init__(self) -> None:
        self.title = "Pybites Python Tips"

    def match_content(self, search: str) -> list[ContentPiece]:
        entries = self.get_data(TIPS_ENDPOINT)
        results = []
        for entry in entries:
            if search.lower() in (entry["title"] + entry["description"]).lower():
                results.append(
                    ContentPiece(
                        title=entry["title"],
                        url=f"{TIPS_URL}{entry['slug']}",
                        channel=self.title,
                    )
                )
        return results


if __name__ == "__main__":
    searcher = TipSearch()
    results = searcher.match_content("unpacking")
    searcher.show_matches(results)
