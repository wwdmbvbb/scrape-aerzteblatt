from datetime import datetime
from typing import Optional

import requests
import re
from bs4 import BeautifulSoup

from consts import base_url
from journals import Journals


class ScrapeArticle:

    def __init__(self, url):
        self._url = url
        self.topics = set()
        self.authors = set()
        self.successful = True
        self.message = None
        self.pdf_link = None
        self.journal_link = None
        self.date: Optional[datetime] = None

        try:
            response = requests.get(self._url)
        except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL,
               requests.exceptions.InvalidSchema) as e:
            self.message = 'Exception: {}'.format(str(e))
            self.successful = False
            return

        if response.status_code < 200 or response.status_code >= 300:
            self.message = 'Got status code {}'.format(response.status_code)
            self.successful = False
            return

        soup = BeautifulSoup(response.text, 'lxml')
        topics = soup.findAll('div', {'class': 'newsThema'})
        if topics is not None and len(topics) > 0:
            for t in topics:
                topic = t.find('a')
                if topic is not None:
                    self.topics.add(topic.string)

        archive_article = soup.find('div', {'class': 'archiveArticleInfo'})
        if archive_article is not None:
            pdf_link = archive_article.find('a', {'class': 'pdfLink'})
            if pdf_link is not None:
                self.pdf_link = base_url + pdf_link['href']

        citation = soup.find('div', {'class': 'citation'})
        if citation is not None:
            authors = citation.findAll('span', {'class': 'author'})
            if authors is not None:
                for a in authors:
                    author = a.find('a')
                    if author is not None:
                        self.authors.add(author.string)

            journal_link = citation.find('a')
            if journal_link is not None:
                link = journal_link['href']
                if link is not None:
                    self.journal_link = link

        news_article = soup.find('div', {'class': 'news'})
        if news_article is not None:
            copyright_spans = news_article.findAll('span', {'class': 'nobr'})
            c_string = None
            if copyright_spans is not None and len(copyright_spans) > 0:
                for span in copyright_spans:
                    if '©' in span.text:
                        c_items = span.find('i')
                        if c_items is not None:
                            c_string = c_items.string
                            break
            else:
                text = news_article.text.replace('Anzeige', '')
                start_index = text.index('©') + 1
                c = text[start_index:]
                end_index = c.find('/aerzteblatt.de')
                if end_index is None:
                    end_index = 20
                c_string = c[:end_index]

            if c_string is not None:
                c_s = [s.strip() for s in c_string.split('/')]
                self.authors = self.authors.union(c_s).difference({'aerzteblatt.de'})

        self.date = Journals().instance.get_journal_date(self.journal_link)
