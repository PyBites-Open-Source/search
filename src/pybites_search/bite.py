from .base import ContentPiece, PybitesSearch

BITES_ENDPOINT = "https://codechalleng.es/api/bites/"
PLATFORM_BASE_URL = "https://codechalleng.es/bites/"


class BiteSearch(PybitesSearch):
    def match_content(self, search: str) -> list[ContentPiece]:
        entries = self.get_data(BITES_ENDPOINT)
        results = []
        for entry in entries:
            if search.lower() in (entry["title"] + entry["description"]).lower():
                results.append(
                    ContentPiece(
                        title=entry["title"],
                        url=f"{PLATFORM_BASE_URL}{entry['number']}",
                    )
                )
        return results


if __name__ == "__main__":
    searcher = BiteSearch()
    results = searcher.match_content("fastapi")
    searcher.show_matches(results)
