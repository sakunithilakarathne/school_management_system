from models.person import *

# Subclass: Teacher
class Teacher(Person):
    def __init__(self, name, age, address, gender, teacher_id, subject):
        super().__init__(name, age, address, gender)  # Inherit common attributes
        self.teacher_id = teacher_id  # Specialized attribute
        self.subject = subject  # Specialized attribute
        self.class_schedule = {}  # Dictionary to store class schedules


    def display_info(self):
        return super().display_info() + f", Teacher ID: {self.teacher_id}, Subject: {self.subject}"


    def role_duties(self):
        return f"Teacher Responsibilities: \n- Teaching {self.subject} \n- Conducting exams for {self.subject}\n"



    def schedule_classes(self, day, time, class_name):
        if day not in self.class_schedule:
            self.class_schedule[day] = {}

        self.class_schedule[day][time] = class_name

    def display_schedule(self):
        """
        Displays the teacher's class schedule.
        """
        if not self.class_schedule:
            return "No classes have been scheduled yet."

        schedule_str = f"Class Schedule for {self.name} (Teacher ID: {self.teacher_id}):\n"
        for day, classes in self.class_schedule.items():
            # schedule_str += f"{day}:\n"
            print(day)
            for time, class_name in classes.items():
                print(f"\t{time} : {class_name}")
        #         schedule_str += f"  {time}: {class_name}\n"
        # return schedule_str