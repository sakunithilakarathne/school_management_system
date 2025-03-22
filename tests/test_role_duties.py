import unittest
from models.student import *
from models.teacher import *
from models.staff import *

class TestRoleDuties(unittest.TestCase):

    # Testing student display_info()
    def test_student_role_duties(self):
        student = Student("Alice Johnson", 16, "456, Garden Road", "Female", "S_001",11)
        self.assertEqual(student.role_duties(), "Student Responsibilities: Maintaining attendance over 80%, Sitting for exams of grade 11\n")

    # Testing teacher display_info()
    def test_teacher_role_duties(self):
        teacher = Teacher("John Smith", 45, "123, School Lane", "Male",
                        "T_001", "Mathematics")
        self.assertEqual(teacher.role_duties(), "Teacher Responsibilities: Teaching Mathematics , Conducting exams for Mathematics\n")

    # Testing staff display_info()
    def test_staff_role_duties(self):
        staff = Staff("Sam Collins", 50, "789, Main Road", "Male",
                  "A_001","Administrator","4","70000","2000")
        self.assertEqual(staff.role_duties(), "Staff Duties: Conducting Administrator related daily duties\n")


    def test_person_role_duties(self):
        """Test role_duties() for the base Person class."""
        person = Person("Austin Cooper", 25, "123 Elm St","Male")
        self.assertEqual(
            person.role_duties(),
            "Adhere to school policies and guidelines\n"
        )



if __name__ == "__main__":
    unittest.main()