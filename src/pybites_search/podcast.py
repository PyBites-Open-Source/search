from .base import ContentPiece, PybitesSearch

PODCAST_ENDPOINT = "https://codechalleng.es/api/podcasts/"
PODCAST_BASE_URL = "https://www.pybitespodcast.com/1501156/"


class PodcastSearch(PybitesSearch):
    def match_content(self, search: str) -> list[ContentPiece]:
        entries = self.get_data(PODCAST_ENDPOINT)
        results = []
        for entry in entries:
            if search.lower() in (entry["title"] + entry["description"]).lower():
                results.append(
                    ContentPiece(
                        title=entry["title"],
                        url=PODCAST_BASE_URL + entry["slug"],
                    )
                )
        return results


if __name__ == "__main__":
    searcher = PodcastSearch()
    results = searcher.match_content("cms")
    searcher.show_matches(results)
