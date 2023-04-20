from .base import ContentPiece, PybitesSearch

YOUTUBE_ENDPOINT = "https://codechalleng.es/api/videos/"
YOUTUBE_BASE_URL = "https://www.youtube.com/watch?v="


class YouTubeSearch(PybitesSearch):
    def match_content(self, search: str) -> list[ContentPiece]:
        entries = self.get_data(YOUTUBE_ENDPOINT)
        results = []
        for entry in entries:
            if search.lower() in (entry["title"] + entry["description"]).lower():
                results.append(
                    ContentPiece(
                        title=entry["title"],
                        url=YOUTUBE_BASE_URL + entry["video_id"],
                    )
                )
        return results


if __name__ == "__main__":
    searcher = YouTubeSearch()
    results = searcher.match_content("django")
    searcher.show_matches(results)
