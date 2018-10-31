class Invite:

    _all = []

    def __init__(self, guest, dinner_party):
        self._guest = guest
        self._rsvp_status = None
        self._dinner_party = dinner_party
        dinner_party._invites.append(self)
        guest._invites.append(self)
        self._all.append(self)

    @property
    def accepted(self):
    # """returns a boolean value (true or false) for whether the the guest accepted the invite or not"""
        return self._rsvp_status
    @property
    def guest(self):
    # """returns the given invite's guest instance"""
        return self._guest
    @property
    def dinner_party(self):
     # """returns the given invite's dinner party instance"""
        return self._dinner_party

    @classmethod
    def all(cls):
    # """returns a list of all invite instances"""
        return cls._all
