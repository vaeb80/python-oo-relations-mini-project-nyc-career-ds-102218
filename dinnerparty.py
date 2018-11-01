
class DinnerParty:
    _all = []

    def __init__(self, name):
        self._name = name
        self._invites = []
        self._courses = []
        self._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    def courses(self):
        return self._courses

    def recipes(self):
        return [course.recipe for course in self.courses()]

    def number_of_attendees(self):
        return len([invite for invite in self.invites if invite.accepted])


    @property
    def invites(self):
        return self._invites

    def guests(self):
        return [invitee.guest.name for invitee in self.invites]

    def reviews(self):
        reviews = []
        for recipe in self.recipes():
            for review in recipe.reviews:
                reviews.append(review)
        return reviews

    def recipe_count(self):
        return len(self.recipes())

    def highest_rated_recipe(self):
        x = [(recipe.avg_review() ,recipe) for recipe in self.recipes()]
        return sorted(x,key=lambda tup:tup[0])[-1][1]
