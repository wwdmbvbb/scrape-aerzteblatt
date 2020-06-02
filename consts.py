import re
from datetime import datetime

base_url = 'https://www.aerzteblatt.de'
search = '/suche'
parameter_name_search = 's'
parameter_name_filter = 'wo'
parameter_name_page = 'page'
search_row_regex = re.compile('jsHitlistData.*')

date_to_number = {
    'Januar': 1,
    'Februar': 2,
    'März': 3,
    'April': 4,
    'Mai': 5,
    'Juni': 6,
    'Juli': 7,
    'August': 8,
    'September': 9,
    'Oktober': 10,
    'November': 11,
    'Dezember': 12
}


def parse_date(date_str: str) -> datetime:
    parts = date_str.split(' ')
    assert len(parts) == 3
    day = parts[0].strip().replace('.', '')
    month = date_to_number[parts[1].strip()]
    year = parts[2].strip()
    return datetime(year=int(year), month=month, day=int(day))
