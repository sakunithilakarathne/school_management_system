from models.person import *

# Subclass: Student
class Student(Person):
    def __init__(self, name, age, address, gender, student_id, year):
        super().__init__(name, age, address, gender)  # Inherit common attributes
        self.year = year
        self.student_id = student_id  # Specialized attribute: Student ID
        self.results = {}  # Dictionary to store grades for subjects
        self.attendance_record = {} # Dictionary to keep attendance record


    def display_info(self):
        return super().display_info() + f", Student ID: {self.student_id}, Class: {self.year}"


    def assign_grades(self, grades):
        """
        Assigns grades for subjects to the student.
        :param grades: A dictionary where keys are subjects (str) and values are grades (int or float).
        :raises ValueError: If the input is invalid (empty, non-numeric grades, or grades outside 0-100).
        """
        if not grades:
            raise ValueError("Grades dictionary cannot be empty.")

        if not isinstance(grades, dict):
            raise ValueError("Input must be a dictionary of subjects and grades.")

        for subject, grade in grades.items():
            if not isinstance(grade, (int, float)):
                raise ValueError(f"Grade for {subject} must be numeric.")

            if grade < 0 or grade > 100:
                raise ValueError(f"Grade for {subject} must be between 0 and 100.")

        self.results = grades


    # Method to calculate the average grade
    def calculate_average_grade(self):
        """
        Calculates the average grade for all subjects.
        :return: The average grade as a float.
        """
        if not self.results:
            raise ValueError("No grades have been assigned yet.")

        total_grades = sum(self.results.values())
        no_of_subjects = len(self.results)
        average_grade = total_grades / no_of_subjects
        return average_grade


    def role_duties(self):
        return f"Student Responsibilities: \n- Maintaining attendance over 80% \n- Sitting for exams of grade {self.year}\n"


    def attendance(self,date,class_name,presence):
        """
        Marks attendance for the student on a specific date and subject.

        :param date: The date of the class (e.g., "2025-01-01").
        :param class_name: The subject of the class (e.g., "Mathematics").
        :param presence: Attendance status (1 for present, 0 for absent).
        """
        if presence > 1 or presence < 0:
            raise ValueError("Status must be 0 (absent) or 1 (present).")

        if date not in self.attendance_record:
            self.attendance_record[date] = {}

        self.attendance_record[date][class_name] = presence


    def calculate_attendance_percentage(self):
        """
        Calculates the overall attendance percentage for the student.
        :return: Attendance percentage as a float.
        """
        if not self.attendance_record:
            return 0.0  # No attendance recorded yet

        total_classes = 0
        present_classes = 0

        for date, subjects in self.attendance_record.items():
            for subject, status in subjects.items():
                total_classes += 1
                if status == 1:
                    present_classes += 1

        return (present_classes / total_classes) * 100

    def display_attendance(self):
        """
        Displays the student's attendance record and overall percentage.
        """
        if not self.attendance_record:
            return "No attendance records found."

        attendance_str = f"Attendance Record for {self.name} (Student ID: {self.student_id}):\n"
        for date, subjects in self.attendance_record.items():
            attendance_str += f"{date}:\n"
            for subject, status in subjects.items():
                attendance_str += f"  {subject}: {'Present' if status == 1 else 'Absent'}\n"

        attendance_percentage = self.calculate_attendance_percentage()
        attendance_str += f"Overall Attendance: {attendance_percentage:.2f}%"

        return attendance_str
