from datetime import datetime
from typing import Optional

import requests
from bs4 import BeautifulSoup

from consts import date_to_number, base_url, parse_date


def _parse(url) -> Optional[datetime]:
    try:
        response = requests.get(base_url + url)
    except(
            requests.exceptions.MissingSchema, requests.exceptions.ConnectionError,
            requests.exceptions.InvalidURL,
            requests.exceptions.InvalidSchema) as e:
        return None

    if response.status_code < 200 or response.status_code >= 300:
        return None

    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.find('div', {'class': 'title'})
    if title is not None:
        date_item = title.find('h2')
        if date_item is not None:
            date = date_item.string
            if ',' in date:
                date = date.split(',')[1].strip()
                return parse_date(date)


class Journals:
    class __Journals:
        def __init__(self):
            self._dates = dict()

        def get_journal_date(self, url) -> Optional[datetime]:
            if url is None:
                return None
            if url in self._dates:
                return self._dates[url]
            else:
                date = _parse(url)
                if date is not None:
                    self._dates[url] = date
                return date

    instance: __Journals = None

    def __init__(self):
        if Journals.instance is None:
            Journals.instance = Journals.__Journals()
