class Categories:
    class __Categories:
        def __init__(self):
            self._categories = dict()
            with open('categories') as f:
                lines = f.readlines()
                for line in lines:
                    items = line.split(':')
                    key = int(items[0].strip())
                    value = items[1].strip()
                    self._categories[key] = value

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


    instance : __Categories = None

    def __init__(self):
        if not Categories.instance:
            Categories.instance = Categories.__Categories()

    def __getattr__(self, item):
        return getattr(self.instance, item)
