from Staff import Staff


class Branch:

    def __init__(self, location):
        self._location = location
        self._staff = []
        self._opening_time = ""

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

    def get_staff(self):
        return self._staff

    def set_opening_time(self, opening_time):
        self._opening_time = opening_time

    def get_opening_time(self):
        return self._opening_time

    def close_branch(self, transfer_branch): # Branch
        for staff in self.get_staff():
            self.transfer_staff_member(transfer_branch, staff)

    def transfer_staff_member(self, to_branch, staff: Staff): # Branch
        self.get_staff().remove(staff)
        to_branch.get_staff().append(staff)
