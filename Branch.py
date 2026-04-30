from Staff import Staff


class Branch:

    def __init__(self, location):
        self._location = location
        self.opening_time = "9:00"
        self._staff = []

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

    def get_opening_time(self):
        return self.opening_time
    
    def set_opening_time(self, opening_time):
        self.opening_time = opening_time

    def get_staff(self):
        return self._staff
    
    def add_staff_member(self, staff: Staff):
        self._staff.append(staff)

    def change_opening_time(self, time: str):
        self.opening_time = time

    def remove_staff(self, staff):
        self._staff.remove(staff)
    
    
