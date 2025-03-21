from models.person import *
from models.student import *
from models.teacher import *
from models.staff import *

if __name__ == "__main__":
    # Create a Student object
    student_1 = Student("Alice Johnson", 16, "456, Galle Road", "Female", "S_001",10)
    print(student_1.display_info())


    # Create a Teacher object
    teacher = Teacher("John Smith", 45, "123, School Lane", "Male","T_001", "Mathematics")
    print(teacher.display_info())


    # Create a Staff object
    staff = Staff("Sam Collins", 50, "789, Main Road", "Male", "A_001","Administrator")
    print(staff.display_info())





