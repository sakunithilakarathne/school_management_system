from dask.array import average

from models.person import *

# Subclass: Student
class Student(Person):
    def __init__(self, name, age, address, gender, student_id, year):
        super().__init__(name, age, address, gender)  # Inherit common attributes
        self.year = year
        self.student_id = student_id  # Specialized attribute: Student ID
        self.results = {}  # Dictionary to store grades for subjects


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