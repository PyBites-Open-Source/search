import re
from html.parser import HTMLParser
from io import StringIO
from pathlib import Path

import feedparser

from .base import ContentPiece, PybitesSearch

PYBITES_PODCAST_FEED = "https://feeds.buzzsprout.com/1501156.rss"
PYBITES_PODCAST_BASE_URL = "https://www.pybitespodcast.com/1501156/"


class MLStripper(HTMLParser):
    """https://stackoverflow.com/a/925630"""

    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


class PodcastSearch(PybitesSearch):
    def match_content(self, search: str) -> list[ContentPiece]:
        term = search.lower()
        re_term = ".*".join(re.split(r"\s+", term))
        results = []

        entries = feedparser.parse(PYBITES_PODCAST_FEED).entries
        for entry in entries:
            summary = strip_tags(entry["summary"])

            title_match = re.search(rf"{re_term}", entry["title"].lower())
            summary_match = re.search(rf"{re_term}", summary.lower())
            if title_match or summary_match:
                if type(entry.links) == list:
                    link = entry.links[0].href
                else:
                    link = entry["link"]

                slug = Path(link.split("/")[-1]).stem
                link = PYBITES_PODCAST_BASE_URL + slug

                results.append(ContentPiece(entry["title"], link))

        return results


if __name__ == "__main__":
    searcher = PodcastSearch()
    results = searcher.match_content("cms")
    searcher.show_matches(results)
