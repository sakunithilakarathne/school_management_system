import unittest
import unittest
from models.student import *
from models.teacher import *
from models.staff import *

class TestStaffSalary(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.staff = Staff("Sam Collins", 50, "789, Main Road", "Male",
                  "A_001","Administrator",4,70000,2000)

    def test_calculate_salary(self):
        """Test the calculate_salary() method."""
        self.staff.calculate_salary()
        self.assertEqual(self.staff.get_salary(), 'Salary: Rs.115000.00')

    def test_get_salary_before_calculation(self):
        """Test the get_salary() method before calculating salary."""
        with self.assertRaises(ValueError):
            self.staff.get_salary()



if __name__ == "__main__":
    unittest.main()