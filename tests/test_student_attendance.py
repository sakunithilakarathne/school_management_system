import unittest
from models.student import *

class TestStudentAttendance(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.student = Student("Ann Davis", 20, "No 1, Lotus Lane", "Female", "S_002", "13")

    def test_attendance(self):
        """Test the attendance() method."""
        self.student.attendance("2025-01-01", "Mathematics", 1)
        self.student.attendance("2025-01-01", "Science", 0)

        # Check if attendance is recorded correctly
        self.assertEqual(self.student.attendance_record["2025-01-01"]["Mathematics"], 1)
        self.assertEqual(self.student.attendance_record["2025-01-01"]["Science"], 0)

    def test_invalid_attendance_status(self):
        """Test the attendance() method with an invalid status."""
        with self.assertRaises(ValueError):
            self.student.attendance("2025-01-01", "Mathematics", 2)  # Invalid status

    def test_calculate_attendance_percentage(self):
        """Test the calculate_attendance_percentage() method."""
        self.student.attendance("2025-01-01", "Mathematics", 1)
        self.student.attendance("2025-01-01", "Science", 0)
        self.student.attendance("2025-01-02", "History", 1)

        # Check attendance percentage
        self.assertAlmostEqual(self.student.calculate_attendance_percentage(), 66.67, places=2)

    def test_calculate_attendance_percentage_no_records(self):
        """Test the calculate_attendance_percentage() method with no records."""
        self.assertEqual(self.student.calculate_attendance_percentage(), 0.0)



    def test_display_attendance_no_records(self):
        """Test the display_attendance() method with no records."""
        self.assertEqual(
            self.student.display_attendance(),
            "No attendance records found."
        )


if __name__ == "__main__":
    unittest.main()