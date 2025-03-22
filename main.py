from models.person import *
from models.student import *
from models.teacher import *
from models.staff import *

if __name__ == "__main__":

    # Create a Student object
    student_1 = Student("Alice Johnson", 16, "456, Garden Road", "Female", "S_001",11)
    student_2 = Student("Ann Davis", 20, "No 1, Lotus Lane", "Female", "S_002", "13")


    # Create a Teacher object
    teacher_1 = Teacher("John Smith", 45, "123, School Lane", "Male",
                        "T_001", "Mathematics")
    teacher_2 = Teacher("Mary Watson", 45, "90, 2nd Lane", "Female",
                        "T_002", "Science")

    # Create a Staff object
    staff_1 = Staff("Sam Collins", 50, "789, Main Road", "Male",
                  "A_001","Administrator",4,70000,2000)
    staff_2 = Staff("Mark Green", 35, "23, Main Road", "Male",
                    "A_002", "HR associate",3,50000,2015)


    # Create a Person object
    person_1 = Person("Carla", 25, "123 Elm St","Female")

    # # Display information
    # print(student_1.display_info())
    # print(teacher_1.display_info())
    # print(staff_1.display_info())
    #
    # # Assign grades for subjects
    # subject_grades = {
    #     "Mathematics": 85,
    #     "Science": 90,
    #     "History": 78,
    #     "English": 88
    # }
    # student_1.assign_grades(subject_grades)
    #
    # # Display grades
    # print("Grades:", student_1.results)
    #
    # # Calculate and display the average grade
    # average_grade = student_1.calculate_average_grade()
    # print(f"Average Grade: {average_grade:.2f}")
    #

    # Getter and Setter for ssn
    # student_2.set_ssn("987654321")
    # teacher_2.set_ssn("456789123")
    #
    # print(student_2.display_info())
    # print("Student SSN:", student_2.get_ssn())
    #
    # print(teacher_2.display_info())
    # print("Teacher SSN:", teacher_2.get_ssn())

    # Display Role Duties
    print(student_2.role_duties())
    print(teacher_2.role_duties())
    print(staff_2.role_duties())
    print(person_1.role_duties())


    # Schedule classes
    # teacher_1.schedule_classes("Monday", "10:00 AM", "Mathematics 101")
    # teacher_1.schedule_classes("Monday", "2:00 PM", "Advanced Calculus")
    # teacher_1.schedule_classes("Wednesday", "9:00 AM", "Linear Algebra")
    #
    # # Display class schedule
    # print(teacher_1.display_schedule())


    # Attendance Tracking
    # Mark attendance
    # student_1.attendance("2025-01-01", "Mathematics", 0)
    # student_1.attendance("2025-01-01", "Science", 1)
    # student_1.attendance("2025-01-01", "Language", 1)
    # student_1.attendance("2025-01-02", "History", 0)
    # student_1.attendance("2025-01-02", "Mathematics", 1)
    # student_1.attendance("2025-01-03", "Science", 1)
    # student_1.attendance("2025-01-03", "Mathematics", 1)
    # student_1.attendance("2025-01-03", "Language", 1)
    #
    # # Display attendance record
    # print(student_1.display_attendance())



    # Calculate salary
    staff_1.calculate_salary()

    #Get salary
    print("Calculated Salary:", staff_1.get_salary())