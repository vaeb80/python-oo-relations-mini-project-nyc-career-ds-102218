class Review:

    _all = []

    def __init__(self, guest, recipe, rating,review):
        self._guest = guest
        self._recipe = recipe
        self._rating = rating
        self._review = review
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
    def guest(self):
        return self._guest
