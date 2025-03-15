from models.person import *

# Subclass: Student
class Student(Person):
    def __init__(self, name, age, address, gender, student_id, grade):
        super().__init__(name, age, address, gender)  # Inherit common attributes
        self.grade = grade
        self.student_id = student_id  # Specialized attribute: Student ID
        self.results = {}  # Dictionary to store grades for subjects
