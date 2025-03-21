import unittest


class TestStaffSalary(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.staff = Staff("Jane Smith", 35, "101 Maple St", "F67890", "Janitorial", 3, 30000)

    def test_calculate_salary(self):
        """Test the calculate_salary() method."""
        self.staff.calculate_salary()

        # Check calculated salary
        # Base Salary: 30000
        # Role Bonus (Janitorial): 2000
        # Years of Service Bonus: 3 * 1000 = 3000
        # Total Salary: 30000 + 2000 + 3000 = 35000
        self.assertEqual(self.staff.get_salary(), 35000)

    def test_get_salary_before_calculation(self):
        """Test the get_salary() method before calculating salary."""
        with self.assertRaises(ValueError):
            self.staff.get_salary()

    def test_display_info(self):
        """Test the display_info() method."""
        self.staff.calculate_salary()

        expected_output = (
            "Name: Jane Smith, Age: 35, Address: 101 Maple St\n"
            "Staff ID: F67890, Role: Janitorial, Years of Service: 3\n"
            "Salary: $35000.00"
        )
        self.assertEqual(self.staff.display_info(), expected_output)

    def test_display_info_no_salary(self):
        """Test the display_info() method before calculating salary."""
        expected_output = (
            "Name: Jane Smith, Age: 35, Address: 101 Maple St\n"
            "Staff ID: F67890, Role: Janitorial, Years of Service: 3\n"
            "Salary: Not calculated yet."
        )
        self.assertEqual(self.staff.display_info(), expected_output)


if __name__ == "__main__":
    unittest.main()