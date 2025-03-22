from models.person import *

# Subclass: Staff
class Staff(Person):
    def __init__(self, name, age, address, gender, staff_id, role, role_grade, base_salary, joined_year):
        super().__init__(name, age, address, gender)  # Inherit common attributes
        self.staff_id = staff_id  # Specialized attribute: Staff ID
        self.role_grade = role_grade
        self.base_salary = base_salary
        self.joined_year = joined_year
        self.role = role
        self.salary = None

    def display_info(self):
        return super().display_info() + f", Staff ID: {self.staff_id}, Role: {self.role}"


    def role_duties(self):
        return f"Staff Duties: Conducting {self.role} related daily duties\n"



    def calculate_salary(self):
        """
        Calculates the salary of the staff member based on role, years of service, and base salary.
        """
        # grade based bonus values
        role_bonus = {
            3 : 15000,
            4 : 20000,
            5 : 30000,
        }.get(self.role_grade, 0)  # Default bonus is 0 if role is not found

        # years of service bonus
        years_of_service = 2025 - self.joined_year
        service_bonus = years_of_service * 1000

        # Calculate total salary
        self.salary = self.base_salary + role_bonus + service_bonus

    def get_salary(self):
        """
        Returns the calculated salary of the staff member.
        :return: The calculated salary as a float.
        """
        if self.salary is None:
            raise ValueError("Salary has not been calculated yet. Call calculate_salary() first.")
        return f"Salary: ${self.salary:.2f}"

