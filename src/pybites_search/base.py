from abc import ABCMeta, abstractmethod
from typing import NamedTuple


class ContentPiece(NamedTuple):
    title: str
    url: str


class PybitesSearch(metaclass=ABCMeta):

    @abstractmethod
    def match_content(self, search: str) -> list[ContentPiece]:
        """Search through Pybites content, implement for a specific source"""

