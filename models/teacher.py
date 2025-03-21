from models.person import *

# Subclass: Teacher
class Teacher(Person):
    def __init__(self, name, age, address, gender, teacher_id, subject):
        super().__init__(name, age, address, gender)  # Inherit common attributes
        self.teacher_id = teacher_id  # Specialized attribute: Teacher ID
        self.subject = subject  # Specialized attribute: Subject taught

    def display_info(self):
        return super().display_info() + f", Teacher ID: {self.teacher_id}, Subject: {self.subject}"


    def role_duties(self):
        return ("\n"
                "- Grading all exams and assignments on time\n"
                "- Conducting in-class lectures\n"
                )