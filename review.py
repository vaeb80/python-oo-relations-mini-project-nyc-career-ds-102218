class Review:

    _all = []

    def __init__(self, guest, recipe, rating,comment):
        self._reviewer = guest
        self._recipe = recipe
        self._rating = rating
        self._comment = comment
        guest._reviews.append(self)
        recipe._reviews.append(self)
        self._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @property
    def rating(self):
        return self._rating
    @property
    def reviewer(self):
        return self._reviewer
    @property
    def recipe(self):
        return self._recipe
    @property
    def comment(self):
        return self._comment
