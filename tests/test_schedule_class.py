import unittest
from models.student import *
from models.teacher import *
from models.staff import *

class TestTeacher(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.teacher = Teacher("John Smith", 45, "123, School Lane", "Male",
                               "T_001", "Mathematics")


    def test_schedule_classes(self):
        """Test the schedule_classes() method."""
        self.teacher.schedule_classes("Monday", "10:00 AM", "Mathematics 101")
        self.teacher.schedule_classes("Monday", "2:00 PM", "Advanced Calculus")

        # Check if classes are scheduled correctly
        self.assertIn("Monday", self.teacher.class_schedule)
        self.assertEqual(self.teacher.class_schedule["Monday"]["10:00 AM"], "Mathematics 101")
        self.assertEqual(self.teacher.class_schedule["Monday"]["2:00 PM"], "Advanced Calculus")

    def test_display_schedule(self):
        """Test the display_schedule() method."""
        self.teacher.schedule_classes("Monday", "10:00 AM", "Mathematics 101")
        self.teacher.schedule_classes("Wednesday", "9:00 AM", "Linear Algebra")

        expected_output = (
            "Class Schedule for John Smith (Teacher ID: T_001):\n"
            "Monday:\n"
            "  10:00 AM: Mathematics 101\n"
            "Wednesday:\n"
            "  9:00 AM: Linear Algebra\n"
        )
        self.assertEqual(self.teacher.display_schedule(), expected_output)

    def test_display_schedule_no_classes(self):
        """Test the display_schedule() method when no classes are scheduled."""
        self.assertEqual(
            self.teacher.display_schedule(),
            "No classes have been scheduled yet."
        )


if __name__ == "__main__":
    unittest.main()