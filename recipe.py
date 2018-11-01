class Recipe:
    _all = []

    def __init__(self, name):
        self._name = name
        self._reviews = []
        self._all.append(self)

    @property
    def reviews(self):
        return self._reviews

    @classmethod
    def all(cls):
        return cls._all

    def avg_review(self):
        if self.reviews:
            total = sum([x.rating for x in self.reviews])
            return total/len(self.reviews)
        else:
            return None

    @classmethod
    def review_recipe(cls):
        x = [(recipe.avg_review(), recipe ) for recipe in cls.all()]
        return list(filter(lambda y: y[0] != None, x))

    def top_five_reviews(self):
        recipes = [(review.rating, review) for review in self.reviews]
        recipes = sorted(recipes, key=lambda tup: tup[0], reverse=True)[:5]
        return [x[1] for x in recipes]

    @classmethod
    def top_three(cls):
        top_recipes = sorted(cls.review_recipe(),key= lambda tup: tup[0])[-3:]
        return [x[1] for x in top_recipes]

    @classmethod
    def bottom_three(cls):
        top_recipes = sorted(cls.review_recipe(),key= lambda tup: tup[0])[:3]
        return [x[1] for x in top_recipes]
