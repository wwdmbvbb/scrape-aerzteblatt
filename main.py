from datetime import datetime

from export import *
from scrape_page import ScrapePage


def search_pages(topic: str, search_cat: int) -> List[AerzteblattResultSet]:
    pages = 1
    page = 1

    results: List[AerzteblattResultSet] = list()
    while pages is not None and page <= pages:
        print('\tSeite {} of {}...'.format(page, pages if pages > 1 else '?'))
        s = ScrapePage(topic, search_cat, page)
        result, pages = s.scrape()

        if not result.success:
            print('\t{}'.format(result.message))
            break

        results.append(result)
        page += 1

    return results


if __name__ == '__main__':
    print('Nach folgenden Kategorien kann gesucht werden:')
    cat = Categories()
    cat.print()

    search_str = input('Suchbegriffe eingeben (durch Komma getrennt):')
    search = [s.strip() for s in search_str.split(',')]

    search_cat_str = input('In welchen Kategorien soll gesucht werden (Zahlen, durch Komma getrennt)')
    search_cats = [int(s) for s in search_cat_str.split(',')]

    for s in search:
        for c in search_cats:
            print('Suche nach "{}" in "{}"'.format(s, cat.instance.name_for_key(c)))
            results = search_pages(search_cat=c, topic=s)
            if len(results) == 0 or len(results[0].results) == 0:
                print('\tKeine Ergebnisse :(')
                continue

            excel = Export([ExportItemExcel(result_set, cat.instance.ref_type_for_key(c), c) for result_set in results])
            print('\tWriting Excel file...')
            excel.write_file('Excel-{}-{}-{}.tsv'.format(s, cat.instance.name_for_key(c), datetime.now()))

            if c in [16, 32, 246, 128, 64, 8]:
                endnote = Export([ExportItemJournalEndnote(result_set, c) for result_set in results])
            else:
                endnote = Export([ExportItemWebEndnote(result_set) for result_set in results])

            print('\tWriting Endnote file...')
            endnote.write_file('Endnote-{}-{}-{}.tsv'.format(s, cat.instance.name_for_key(c), datetime.now()))
