import unittest
from models.student import *

class TestStudentGrades(unittest.TestCase):
    def test_valid_values_for_assign_grades(self):
        """Test assigning a valid grades."""
        student = Student("Alice Johnson", 16, "456, Garden Road", "Female", "S_001",11)
        subject_grades = {
            "Mathematics": 85,
            "Science": 90,
            "History": 78,
            "English": 88
        }
        student.assign_grades(subject_grades)
        self.assertEqual(student.results, subject_grades)


    def test_calculate_average_grade(self):
        """Test calculating average when dictionary is not empty."""
        student = Student("Alice Johnson", 16, "456, Garden Road", "Female", "S_001",11)
        subject_grades = {
            "Mathematics": 85,
            "Science": 90,
            "History": 78,
            "English": 88
        }
        student.assign_grades(subject_grades)
        self.assertAlmostEqual(student.calculate_average_grade(), 85.25)


    def test_invalid_values_for_assign_grades(self):
        """Test assigning a invalid grades."""
        student = Student("Alice Johnson", 16, "456, Garden Road", "Female", "S_001",11)
        with self.assertRaises(ValueError):
            student.assign_grades({"Mathematics": 105})  # Invalid grade
        with self.assertRaises(ValueError):
            student.assign_grades("Not a dictionary")  # Invalid input type


    def test_calculate_average_with_no_grades(self):
        """Test calculating average when dictionary is empty"""
        student = Student("Alice Johnson", 16, "456, Garden Road", "Female", "S_001",11)
        with self.assertRaises(ValueError):
            student.calculate_average_grade()  # No grades assigned

if __name__ == "__main__":
    unittest.main()