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
    # """returns a list of all of the guest's invites"""
        return self._invites
    def reviews(self):
        # """returns a list of all of the guest's reviews """
        return self._reviews
    def number_of_invites(self):
        # """returns the number of dinner party invites a guest has recieved"""
        return len(self._invites)
    def rsvp(self, invite, rsvp_status):
        # """takes in a boolean value (True or False) and updates a guest's rsvp
        # status. It should return the rsvp_status status """
        invite._rsvp_status = rsvp_status
        return invite.accepted
    def review_recipe(self, recipe, rating, comment):
        # """adds a guest's review with a rating and comment to a recipe."""
        # """Returns the given recipe's reviews """
        pass

    def favorite_recipe(self):
     # """returns the given guest's favorite recipe"""
        pass

    @classmethod
    def all(cls):
        return cls._all
    @classmethod
    def most_popular(cls):
    # """returns guest invited to most dinner parties"""
        all_invites = [(guest.count, guest) for guest in cls.all()]
        sorted_invites = sorted(all_invites,key=lambda tup: tup[0], reverse=True)
        return sorted_invites[0][1]

    @classmethod
    def toughest_critic(cls):
    # """returns guest with lowest avg rating for recipe reviews"""
        avg_review_guests = [(guest.avg_review(), guest) for guest in cls.all() ]
        sorted_reviews = sorted(avg_review_guests, key=lambda tup: tup[0])
        return sorted_reviews[0][1]
    @classmethod
    def most_active_critic(cls):
    # """returns guest with most recipe reviews"""
        all_reviews = [(len(guest._reviews), guest) for guest in cls.all()]
        sorted_reviews= sorted(all_reviews,key=lambda tup: tup[0], reverse=True)
        return sorted_reviews[0][1]
