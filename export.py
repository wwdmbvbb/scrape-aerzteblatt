import os
from datetime import datetime
from typing import Set, List

from categories import Categories
from results import AerzteblattResultSet


class ExportItem:

    def __init__(self, result: AerzteblattResultSet):
        self._result = result
        assert self._result.success
        self._separator = '\t'
        self._title = None
        self._and_symbol = None

    def _generate_headings(self) -> [str]:
        raise NotImplementedError()

    def _generate_rows(self) -> [[str]]:
        raise NotImplementedError()

    def _process_set(self, items: Set[str]) -> str:
        assert self._and_symbol is not None
        if items is None:
            return ''
        return ' {} '.format(self._and_symbol).join(items)

    def _process_authors(self, authors: Set[str]) -> str:
        s = self._process_set(authors)
        # hacky postprocessing
        if len(s.replace('©', '').strip()) == 0 or len(s) >= 300:
            return ''
        return self._process_set(authors)

    def get_lines(self) -> List[str]:
        return [self._separator.join(row) + '\n' for row in
                self._generate_rows()]

    @property
    def header(self) -> str:
        begin = ''
        if self._title is not None:
            begin = '*{}\n'.format(self._title)
        return begin + self._separator.join(self._generate_headings()) + '\n'

    def _clean_list(self, l):
        return list([item if item is not None else '' for item in l])


class ExportItemJournalEndnote(ExportItem):
    def __init__(self, result: AerzteblattResultSet, cat_id: int):
        super().__init__(result)
        self._title = 'Journal Article'
        self._and_symbol = '//'
        self._cat_id = cat_id

    def _generate_headings(self) -> List[str]:
        return ['Author', 'Year', 'Title', 'Journal', 'Volume', 'Issue', 'Pages', 'Date', 'Label', 'Keywords', 'URL']

    def _generate_rows(self) -> List[List[str]]:
        rows = list()
        for item in self._result.results:
            authors = self._process_authors(item.authors)
            topics = self._process_set(item.topics)
            src_info = item.source.data
            rows.append(self._clean_list(
                [authors, src_info.year, item.title, self._journal_title(), src_info.volume, src_info.number,
                 src_info.page, src_info.date, item.category, topics, item.url]))
        return None if len(rows) < 1 else rows

    def _journal_title(self):
        if self._cat_id == 32:
            return 'Deutsches Ärzteblatt PP'
        else:
            return 'Deutsches Ärzteblatt'


class ExportItemWebEndnote(ExportItem):
    def __init__(self, result: AerzteblattResultSet):
        super().__init__(result)
        self._title = 'Web Page'
        self._and_symbol = '//'

    def _generate_headings(self) -> List[str]:
        return ['Author', 'Title', 'Last Update Date', 'Label', 'Keywords', 'URL']

    def _generate_rows(self) -> List[List[str]]:
        rows = list()
        for item in self._result.results:
            authors = self._process_authors(item.authors)
            topics = self._process_set(item.topics)
            src_info = item.source.data
            rows.append(
                self._clean_list([authors, item.title, src_info.date, item.category, topics, item.url]))
        return None if len(rows) < 1 else rows


class ExportItemExcel(ExportItemJournalEndnote):
    def __init__(self, result: AerzteblattResultSet, ref_type: str, cat_id: int):
        super().__init__(result, cat_id)
        self._ref_type = ref_type
        self._and_symbol = ';'
        self._title = None

    def _generate_headings(self) -> [str]:
        return ['Erscheinungsdatum', 'Jahr', 'Autor', 'Titel', 'Label', 'Fachbereich', 'Referenztyp', 'Stichworte',
                'Journal', 'Jahrgang', 'Heft', 'Seite', 'DOI', 'PDF']

    def _generate_rows(self) -> [[str]]:
        rows = list()
        for item in self._result.results:
            authors = self._process_authors(item.authors)
            topics = self._process_set(item.topics)
            src_info = item.source.data
            rows.append(self._clean_list(
                [src_info.date, src_info.year, authors, item.title, item.category,
                 Categories().instance.name_for_key(self._cat_id), self._ref_type,
                 topics,
                 self._journal_title(), src_info.volume, src_info.number, src_info.page, src_info.doi, item.pdf]))
        return None if len(rows) < 1 else rows


class Export:

    def __init__(self, items: List[ExportItem], path: str = '~/Downloads/Aerzteblatt'):
        self._items: List[ExportItem] = items
        self._path = path

    def write_file(self, file_name: str):
        if len(self._items) == 0:
            print('no items to export for {}'.format(file_name))
            return

        header = self._items[0].header
        path = self._path.replace('~', os.path.expanduser('~')) + '/' + file_name
        dirname = os.path.dirname(path)
        os.makedirs(dirname, exist_ok=True)
        with open(path, 'x') as file:
            file.write(header)
            for item in self._items:
                lines = item.get_lines()
                file.writelines(lines)
