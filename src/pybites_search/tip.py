from .base import ContentPiece, PybitesSearch

TIPS_ENDPOINT = "https://codechalleng.es/api/pytips/"


class TipSearch(PybitesSearch):
    def match_content(self, search: str) -> list[ContentPiece]:
        entries = self.get_data(TIPS_ENDPOINT)
        results = []
        for entry in entries:
            if search.lower() in (entry["title"] + entry["description"]).lower():
                results.append(
                    ContentPiece(
                        title=entry["title"],
                        url=entry["link"],
                    )
                )
        return results


if __name__ == "__main__":
    searcher = TipSearch()
    results = searcher.match_content("unpacking")
    searcher.show_matches(results)
