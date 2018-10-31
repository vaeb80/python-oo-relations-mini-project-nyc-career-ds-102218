class Recipe:
    _all = []

    def __init__(self, name):
        self._name = name
        self._reviews = []
        self._all.append(self)
