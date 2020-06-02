import requests
from bs4 import BeautifulSoup

from consts import *
from results import AerzteblattResultSet, AerzteblattResult
from urllib.parse import quote_plus


class ScrapePage:

    def __init__(self, search_string: str = '', search_cat: int = None, page: int = 1):
        filter_str = '' if search_cat is None else '&{}={}'.format(parameter_name_filter, search_cat)
        self._url = '{}{}?{}={}{}&{}={}'.format(base_url, search, parameter_name_search,
                                                quote_plus(search_string.encode('iso-8859-1')),
                                                filter_str,
                                                parameter_name_page, page)
        self._search_cat = search_cat

    def scrape(self) -> (AerzteblattResultSet, int):
        try:
            response = requests.get(self._url)
        except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL,
               requests.exceptions.InvalidSchema) as e:
            return AerzteblattResultSet(False, 'Request threw an exception, Exception: {}'.format(e)), None

        if response.status_code < 200 or response.status_code >= 300:
            return AerzteblattResultSet(False, 'Request was not successful ({})'.format(response.status_code)), None

        soup = BeautifulSoup(response.text, 'lxml')
        # soup = BeautifulSoup(text, 'lxml')
        pages_div = soup.find('div', {'class': 'navigator'})
        results_div = soup.find('div', {'class': 'jsHitlist'})

        if results_div is None or pages_div is None:
            return AerzteblattResultSet(False, 'Could not find search result list'), None

        result_set = AerzteblattResultSet()
        rows = results_div.findAll('div', {'class': search_row_regex})
        for row in rows:
            result_set.add(AerzteblattResult(row, self._search_cat))

        return result_set, int(pages_div['data-pagecount'])
