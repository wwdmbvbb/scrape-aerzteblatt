import re
from datetime import datetime
from enum import Enum
from typing import Optional, Union

from consts import date_to_number, parse_date


class Semantic(Enum):
    YEAR = 1,
    VOLUME = 2,
    NUMBER = 3,
    PAGE = 4,
    DOI = 5,
    DATE = 6,
    UNKNOWN = 7,


class SrcInfo:

    def __init__(self, year: str = None, volume: str = None, number: str = None, page: str = None, doi: str = None,
                 date: str = None):
        self._year: Optional[str] = year
        self.volume: Optional[str] = volume
        self.number: Optional[str] = number
        self.page: Optional[str] = page
        self.doi: Optional[str] = doi
        self._date: Optional[datetime] = date

    @property
    def date(self) -> Optional[str]:
        if self._date is None:
            return None
        return self._date.strftime('%Y-%m-%d')

    @date.setter
    def date(self, value: Union[None, str, datetime]):
        if type(value) is str:
            self._date = parse_date(value)
        else:
            self._date = value

    @property
    def year(self) -> Optional[str]:
        if self._year is not None:
            return self._year
        elif self._date is not None:
            return str(self._date.year)
        else:
            return None

    def __str__(self):
        return """  year: {}
          volume: {}
          number: {}
          page: {}
          doi: {}
          date: {}
        """.format(self.year, self.volume, self.number, self.page, self.doi, self.date)


class SrcParser:
    _patterns = {
        # Deutsches Ärzteblatt
        16: (re.compile('.*?(\d*);\s*(\d*)\(([\d-]*)\):(?:\s*A-(\d*)|(?:\s*\[(\d*)\]))'),
             (Semantic.YEAR, Semantic.VOLUME, Semantic.NUMBER, Semantic.PAGE, Semantic.PAGE)),
        # Dtsch Arztebl 2020; 117(21): A-1128 / B-947
        # Deutsches Ärzteblatt PP
        32: (re.compile(
            '.*?(\d*),\s*Ausgabe\s*(.*?\s*\d*),\s*Seite\s*(\d*)'), (Semantic.VOLUME, Semantic.NUMBER, Semantic.PAGE)),
        # PP 19, Ausgabe Mai 2020, Seite 203
        # Perspektiven
        256: (re.compile(
            '.*?(\d*);\s*(\d*)\((\d*)\):\s*\[(\d*)\](;\s*DOI:\s*(.*))?'),
              (Semantic.YEAR, Semantic.VOLUME, Semantic.NUMBER, Semantic.UNKNOWN, None, Semantic.DOI)),
        # Dtsch Arztebl 2020; 117(20): [4]; DOI: 10.3238/PersDia.2020.05.15.01
        # Praxis
        128: (re.compile(
            '.*?(\d*);\s*(\d*)\((\d*)\):\s*\[(\d*)\](;\s*DOI:\s*(.*))?'),
              (Semantic.YEAR, Semantic.VOLUME, Semantic.NUMBER, Semantic.UNKNOWN, None, Semantic.DOI)),
        # Dtsch Arztebl 2020; 117(20): [4]; DOI: 10.3238/PersDia.2020.05.15.01
        # Medizin studieren
        64: (re.compile('.*([WS]S\s*[\d/]*):\s*(\d*)'), (Semantic.VOLUME, Semantic.NUMBER)),
        # Medizin studieren, WS 2019/20: 30
        # News
        1: (re.compile('.*?,.*?,\s*(\d*.\s*.*\d*)'), Semantic.DATE),  # News, Mittwoch, 20. Mai 2020
        # Blogs
        2: (re.compile('.*?,.*?,\s*(\d*.\s*.*\d*)'), Semantic.DATE),
        # Preise
        8: (re.compile('.*?,.*?,\s*(\d*.\s*.*\d*)'), Semantic.DATE),
        # Foren
        4: (re.compile('.*?,\s*(\d*\.\d*\.\d*)\s*\d{2}:\d{2}'), Semantic.DATE)  # Foren, 21.05.20 14:02
    }

    def __init__(self, src_string: str, category: int):
        matcher, semantic = SrcParser._patterns[category]
        self.data: SrcInfo = SrcInfo()
        self._category = category

        if matcher is None or semantic is None or src_string is None:
            return

        result = matcher.match(src_string)
        if result is None:
            return
        self._process_result(result.groups(), semantic)

    def _process_result(self, groups, semantic):
        if type(semantic) is tuple:
            assert len(semantic) == len(groups)
            for i in range(len(semantic)):
                self._process_item(semantic[i], groups[i])
        else:
            self._process_item(semantic, groups[0])
        self._post_process_item()

    def _process_item(self, semantic, value: Optional[str]):
        if semantic is Semantic.VOLUME and value is not None:
            self.data.volume = value
        elif semantic is Semantic.DATE and value is not None:
            self.data.date = value
        elif semantic is Semantic.NUMBER and value is not None:
            self.data.number = value
        elif semantic is Semantic.YEAR and value is not None:
            self.data._year = value
        elif semantic is Semantic.DOI and value is not None:
            self.data.doi = value
        elif semantic is Semantic.PAGE and value is not None:
            self.data.page = value

    def _post_process_item(self):
        if self._category == 32:  # PP
            split_number = self.data.number.split(' ')
            if split_number is not None and len(split_number) == 2:
                self.data._year = split_number[1]
                nr = date_to_number.get(split_number[0], None)
                if nr is not None:
                    self.data.number = '{}/{}'.format(nr, self.data._year)

    def __str__(self):
        return str(self.data)
