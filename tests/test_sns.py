import unittest
from models.student import *
from models.teacher import *
from models.staff import *


class TestPerson(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.person = Person("Carla", 25, "123 Elm St","Female")
        self.student = Student("Alice Johnson", 16, "456, Garden Road", "Female", "S_001",11)
        self.teacher = Teacher("John Smith", 45, "123, School Lane", "Male",
                        "T_001", "Mathematics")

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





if __name__ == "__main__":
    unittest.main()