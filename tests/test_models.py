import unittest

class TestSchoolClasses(unittest.TestCase):
    def test_student(self):
        student = Student("Alice", 16, "123 Elm St", "S12345")
        self.assertEqual(student.display_info(), "Name: Alice, Age: 16, Address: 123 Elm St, Student ID: S12345")
        self.assertEqual(student.role_duties(), "Responsibilities: Attend classes, complete assignments, and participate in exams.")

    def test_teacher(self):
        teacher = Teacher("Mr. Smith", 45, "456 Oak St", "T98765", "Mathematics")
        self.assertEqual(teacher.display_info(), "Name: Mr. Smith, Age: 45, Address: 456 Oak St, Teacher ID: T98765, Subject: Mathematics")
        self.assertEqual(teacher.role_duties(), "Responsibilities: Teach Mathematics, grade assignments, and manage classes.")

    def test_staff(self):
        staff = Staff("John Doe", 30, "789 Pine St", "F54321", "Administrative")
        self.assertEqual(staff.display_info(), "Name: John Doe, Age: 30, Address: 789 Pine St, Staff ID: F54321, Role: Administrative")
        self.assertEqual(staff.role_duties(), "Responsibilities: Manage Administrative tasks and support school operations.")

if __name__ == "__main__":
    unittest.main()