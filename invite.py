from dinnerparty import DinnerParty
class Invite:

    _all = []

    def __init__(self, dinner_party, guest):
        self._guest = guest
        self._rsvp_status = None
        self._dinner_party = dinner_party
        guest._invites.append(self)
        dinner_party._invites.append(self)
        self._all.append(self)

    @property
    def accepted(self):
        return self._rsvp_status
    @accepted.setter
    def accepted(self, rsvp_status):
        self._rsvp_status = rsvp_status
    @property
    def guest(self):
        return self._guest
    @property
    def dinner_party(self):
        return self._dinner_party

    @classmethod
    def all(cls):
        return cls._all
