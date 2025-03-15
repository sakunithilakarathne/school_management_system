from models.person import *

# Subclass: Staff
class Staff(Person):
    def __init__(self, name, age, address, gender, ssn, staff_id, role):
        super().__init__(name, age, address, gender)  # Inherit common attributes
        self.ssn = ssn
        self.staff_id = staff_id  # Specialized attribute: Staff ID
        self.role = role  # Specialized attribute: Role (e.g., administrative, janitorial)