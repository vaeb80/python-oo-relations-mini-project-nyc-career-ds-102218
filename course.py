class Course:

    _all = []

    def __init__(self, dinner_party, recipe):
        self._dinner_party = dinner_party
        self._recipe = recipe
        dinner_party._courses.append(self)
        self._all.append(all)

    @property
    def dinner_party(self):
        return self._dinner_party

    @property
    def recipe(self):
        return self._recipe

    @classmethod
    def all(cls):
        return cls._all
