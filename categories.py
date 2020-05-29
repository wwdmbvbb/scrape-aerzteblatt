class Categories:
    class __Categories:
        def __init__(self):
            self._categories = {16: 'Deutsches Ärzteblatt',
                                32: 'Deutsches Ärzteblatt PP',
                                256: 'Perspektiven',
                                128: 'Praxis',
                                64: 'Medizin Studieren',
                                1: 'News',
                                2: 'Blogs',
                                4: 'Foren',
                                8: 'Preise'}

        def print(self):
            print('Kategorien: ')
            for key in self._categories.keys():
                print('{} ({})'.format(self._categories[key], key))

        def name_for_key(self, key):
            return self._categories[key] if key in self._categories else None

        def all_categories(self):
            return self._categories.keys()

        def ref_type_for_key(self, key):
            if key in [1, 2, 4]:
                return 'Web Page'
            else:
                return 'Journal Article'

    instance: __Categories = None

    def __init__(self):
        if not Categories.instance:
            Categories.instance = Categories.__Categories()

    def __getattr__(self, item):
        return getattr(self.instance, item)
