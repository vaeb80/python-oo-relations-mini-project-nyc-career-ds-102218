class DinnerParty:
    _all = []

    def __init__(self, name):
        self._name = name
        self._invites = []
        self._reviews = []
        self._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    def invites(self):
        return self._invites

    def guests(self):
        return [invitee.guest.name for invitee in self.invites()]

    def reviews(self):
        return self._reviews
