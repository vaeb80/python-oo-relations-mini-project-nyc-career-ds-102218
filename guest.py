from review import Review

class Guest:

    _all = []

    def __init__(self, name):
        self._name = name
        self._invites = []
        self._reviews = []
        self._count = len(self._invites)
        self._all.append(self)

    @property
    def name(self):
        return self._name
    @property
    def count(self):
        return self._count

    def avg_review(self):
        total = sum([x._rating for x in self.reviews()])
        return total/len(self._reviews)

    def invites(self):
        return self._invites

    def reviews(self):
        return self._reviews

    def number_of_invites(self):
        return len(self._invites)

    def rsvp(self, invite, rsvp_status):
        invite.accepted = rsvp_status
        return invite.accepted

    def review_recipe(self, recipe, rating, comment):
            Review(self, recipe, rating, comment)
            return recipe.reviews


    def favorite_recipe(self):
        rating_review = list(map(lambda review: (review.rating, review.recipe), self._reviews))
        return sorted(rating_review, key=lambda tup: tup[0], reverse=True)[0][1]

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def most_popular(cls):
        all_invites = [(guest.count, guest) for guest in cls.all()]
        sorted_invites = sorted(all_invites,key=lambda tup: tup[0], reverse=True)
        return sorted_invites[0][1]

    @classmethod
    def toughest_critic(cls):
        avg_review_guests = [(guest.avg_review(), guest) for guest in cls.all() ]
        sorted_reviews = sorted(avg_review_guests, key=lambda tup: tup[0])
        return sorted_reviews[0][1]

    @classmethod
    def most_active_critic(cls):
        all_reviews = [(len(guest._reviews), guest) for guest in cls.all()]
        sorted_reviews= sorted(all_reviews,key=lambda tup: tup[0], reverse=True)
        return sorted_reviews[0][1]
