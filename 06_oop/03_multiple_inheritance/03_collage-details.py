'''###############output#########
===== STUDENT FULL DETAILS =====
College Name : Takshshilla Institute of Engineering and Technology
Location     : Jabalpur
Student Name : Krishna Kewat
Course       : B.Tech CSE
CGPA         : 8.15
##############################'''
# Parent class 1
class College:
    def __init__(self, college_name, location):
        self.college_name = college_name
        self.location = location


# Parent class 2
class Student:
    def __init__(self, student_name, course):
        self.student_name = student_name
        self.course = course


# Parent class 3
class Result:
    def __init__(self, cgpa):
        self.cgpa = cgpa


# Child class (Multiple Inheritance)
class StudentRecord(College, Student, Result):
    def __init__(self, college_name, location, student_name, course, cgpa):
        College.__init__(self, college_name, location)
        Student.__init__(self, student_name, course)
        Result.__init__(self, cgpa)

    def display(self): # here we are displaying the full details of the student by accessing attributes from all parent classes 
        print("===== STUDENT FULL DETAILS =====")
        print(f"College Name : {self.college_name}")
        print(f"Location     : {self.location}")
        print(f"Student Name : {self.student_name}")
        print(f"Course       : {self.course}")
        print(f"CGPA         : {self.cgpa}")


# Object creation (your data)
s1 = StudentRecord(
    "Takshshilla Institute of Engineering and Technology",
    "Jabalpur",
    "Krishna Kewat",
    "B.Tech CSE",
    8.15
)

# Display output
s1.display()