from models.person import *

# Subclass: Teacher
class Teacher(Person):
    def __init__(self, name, age, address, gender, ssn, teacher_id, subject):
        super().__init__(name, age, address, gender)  # Inherit common attributes
        self.ssn = ssn
        self.teacher_id = teacher_id  # Specialized attribute: Teacher ID
        self.subject = subject  # Specialized attribute: Subject taught