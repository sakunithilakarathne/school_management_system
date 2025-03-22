import unittest
from models.person import *
from models.student import *
from models.teacher import *
from models.staff import *



class TestSchoolClasses(unittest.TestCase):


    # Testing student display_info()
    def test_student(self):
        student = Student("Alice Johnson", 16, "456, Garden Road", "Female", "S_001",11)
        self.assertEqual(student.display_info(), "Name: Alice Johnson, Age: 16, Address: 456, Garden Road, Student ID: S_001, Class: 11")


    # Testing teacher display_info()
    def test_teacher(self):
        teacher = Teacher("John Smith", 45, "123, School Lane", "Male",
                        "T_001", "Mathematics")
        self.assertEqual(teacher.display_info(), "Name: John Smith, Age: 45, Address: 123, School Lane, Teacher ID: T_001, Subject: Mathematics")


    # Testing staff display_info()
    def test_staff(self):
        staff = Staff("Sam Collins", 50, "789, Main Road", "Male",
                  "A_001","Administrator","4","70000","2000")
        self.assertEqual(staff.display_info(), "Name: Sam Collins, Age: 50, Address: 789, Main Road, Staff ID: A_001, Role: Administrator")





if __name__ == "__main__":
    unittest.main()