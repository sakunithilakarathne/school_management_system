import unittest

class TestPerson(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.person = Person("Alice", 25, "123 Elm St")
        self.student = Student("Bob", 20, "456 Oak St", "S12345")
        self.teacher = Teacher("Mr. Smith", 45, "789 Pine St", "T98765", "Mathematics")

    def test_set_valid_ssn(self):
        """Test setting a valid SSN."""
        self.person.set_ssn("123456789")
        self.assertEqual(self.person.get_ssn(), "123456789")

        self.student.set_ssn("987654321")
        self.assertEqual(self.student.get_ssn(), "987654321")

        self.teacher.set_ssn("456789123")
        self.assertEqual(self.teacher.get_ssn(), "456789123")

    def test_set_invalid_ssn(self):
        """Test setting an invalid SSN."""
        with self.assertRaises(ValueError):
            self.person.set_ssn("12345")  # Too short

        with self.assertRaises(ValueError):
            self.person.set_ssn("1234567890")  # Too long

        with self.assertRaises(ValueError):
            self.person.set_ssn("123-45-678")  # Contains non-digits

        with self.assertRaises(ValueError):
            self.person.set_ssn(123456789)  # Not a string

    def test_get_ssn_before_setting(self):
        """Test getting SSN before it is set."""
        self.assertIsNone(self.person.get_ssn())
        self.assertIsNone(self.student.get_ssn())
        self.assertIsNone(self.teacher.get_ssn())

    def test_display_info(self):
        """Test the display_info method."""
        self.assertEqual(
            self.person.display_info(),
            "Name: Alice, Age: 25, Address: 123 Elm St"
        )
        self.assertEqual(
            self.student.display_info(),
            "Name: Bob, Age: 20, Address: 456 Oak St"
        )
        self.assertEqual(
            self.teacher.display_info(),
            "Name: Mr. Smith, Age: 45, Address: 789 Pine St"
        )

    def test_student_specific_attributes(self):
        """Test Student-specific attributes."""
        self.assertEqual(self.student.student_id, "S12345")

    def test_teacher_specific_attributes(self):
        """Test Teacher-specific attributes."""
        self.assertEqual(self.teacher.teacher_id, "T98765")
        self.assertEqual(self.teacher.subject, "Mathematics")


if __name__ == "__main__":
    unittest.main()