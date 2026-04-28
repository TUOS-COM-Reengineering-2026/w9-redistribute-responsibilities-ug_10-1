from Staff import Staff


class Branch:

    def __init__(self, location):
        self._location = location
        self._staff = []

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

    def get_staff(self):
        return self._staff
    
    def add_staff_member(self, staff):
        self._staff.append(staff)
    
    def remove_staff_member(self, staff):
        self._staff.remove(staff)
