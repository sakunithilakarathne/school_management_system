import unittest

class TestRoleDuties(unittest.TestCase):
    def test_person_role_duties(self):
        """Test role_duties() for the base Person class."""
        person = Person("Alice", 25, "123 Elm St")
        self.assertEqual(
            person.role_duties(),
            "General responsibilities: Contribute to the school community."
        )

    def test_student_role_duties(self):
        """Test role_duties() for the Student class."""
        student = Student("Bob", 20, "456 Oak St", "S12345")
        self.assertEqual(
            student.role_duties(),
            "Responsibilities: Attend classes, complete assignments, and participate in exams."
        )

    def test_teacher_role_duties(self):
        """Test role_duties() for the Teacher class."""
        teacher = Teacher("Mr. Smith", 45, "789 Pine St", "T98765", "Mathematics")
        self.assertEqual(
            teacher.role_duties(),
            "Responsibilities: Teach Mathematics, grade assignments, and manage classes."
        )

    def test_staff_role_duties(self):
        """Test role_duties() for the Staff class."""
        staff = Staff("John Doe", 30, "101 Maple St", "F54321", "Administrative")
        self.assertEqual(
            staff.role_duties(),
            "Responsibilities: Manage Administrative tasks and support school operations."
        )


if __name__ == "__main__":
    unittest.main()