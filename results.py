import string
from typing import Set, Union

from consts import base_url
from scrape_article import ScrapeArticle
from src_parser import SrcParser


class AerzteblattResult:

    def __init__(self, tag, search_cat):
        category = tag.find('div', {'class': 'jsHitlistCategory'})
        self.category: Union[None, str] = None
        self.url: Union[None, str] = None
        self.title: Union[None, str] = None
        self._author = None
        self.source: Union[SrcParser, None] = None
        self._authors = None
        self._topics: Union[None, Set[str]] = None
        self.pdf: Union[None, str] = None

        if category is not None:
            self.category = string.capwords(category.string)

        title = tag.find('div', {'class': 'jsHitlistTitle'}).find('a')
        if title is not None:
            self.title = title.string
            self.url = '{}/{}'.format(base_url, title['href'])

        author = tag.find('div', {'class': 'jsHitlistAuthor'}).find('span', {'class': 'author'})
        if author is not None:
            self._author = author.string

        src = tag.find('div', {'class': 'jsHitlistSrc'})
        if src is not None:
            self.source = SrcParser(src.string, search_cat)

        # MUST BE CALLED after self.source was defined
        if self.url is not None:
            self._parse_url()

    def __str__(self):
        return """ Aerzteblatt Result:
          category: {}
          title: {}
          author: {}
          url: {}
          authors: {}
          topics: {}
          pdf: {}
          source: {}
        """.format(self.category, self.title, self._author, self.url, self._authors, self._topics, self.pdf,
                   str(self.source))

    def _parse_url(self):
        s = ScrapeArticle(self.url)
        self._authors = s.authors
        self._topics = s.topics
        self.pdf = s.pdf_link
        if s.date is not None and self.source is not None and self.source.data.date is None:
            self.source.data.date = s.date

    @property
    def authors(self):
        if self._authors is not None and len(self._authors) > 0:
            return self._authors
        elif self._author is not None:
            return {self._author}
        else:
            return None

    @property
    def topics(self):
        return None if len(self._topics) < 1 else self._topics


class AerzteblattResultSet:

    def __init__(self, success: bool = True, message: str = 'success'):
        self._results: Set[AerzteblattResult] = set()
        self.message = message
        self.success = success

    def add(self, result: AerzteblattResult):
        self._results.add(result)

    @property
    def results(self) -> Set[AerzteblattResult]:
        return self._results

    def __str__(self):
        s = ''
        for result in self._results:
            s += str(result)
        return s
