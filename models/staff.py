from models.person import *

# Subclass: Staff
class Staff(Person):
    def __init__(self, name, age, address, gender, staff_id, role):
        super().__init__(name, age, address, gender)  # Inherit common attributes
        self.staff_id = staff_id  # Specialized attribute: Staff ID
        self.role = role  # Specialized attribute: Role (e.g., administrative, janitorial)

    def display_info(self):
        return super().display_info() + f", Staff ID: {self.staff_id}, Role: {self.role}"


    def role_duties(self):
        return f"Staff Duties: \n-Conducting {self.role} related daily duties\n"