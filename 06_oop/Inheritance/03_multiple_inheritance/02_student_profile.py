'''###############output#########
===== Student Profile =====
----- Student Info -----
Name      : Krishna Kewat
Roll No   : 21
Class     : 12th Science
----- Exam Info -----
Marks     : 88
Grade     : A
----- Sports Info -----
Sport     : Cricket
Level     : District Level
##############################'''
# Parent class 1
class Student:
    def __init__(self, name, roll_no, class_name):
        self.name = name
        self.roll_no = roll_no
        self.class_name = class_name

    def show_student(self):
        print("----- Student Info -----")
        print(f"Name      : {self.name}")
        print(f"Roll No   : {self.roll_no}")
        print(f"Class     : {self.class_name}")


# Parent class 2
class Exam:
    def __init__(self, marks, grade):
        self.marks = marks
        self.grade = grade

    def show_exam(self):
        print("----- Exam Info -----")
        print(f"Marks     : {self.marks}")
        print(f"Grade     : {self.grade}")


# Parent class 3
class Sports:
    def __init__(self, sport_name, level):
        self.sport_name = sport_name
        self.level = level

    def show_sports(self):
        print("----- Sports Info -----")
        print(f"Sport     : {self.sport_name}")
        print(f"Level     : {self.level}")


# Child class (Multiple Inheritance)
class StudentProfile(Student, Exam, Sports):
    def __init__(self, name, roll_no, class_name, marks, grade, sport_name, level):
        Student.__init__(self, name, roll_no, class_name)
        Exam.__init__(self, marks, grade)
        Sports.__init__(self, sport_name, level)

    def show_profile(self):
        print("\n===== Student Profile =====")
        self.show_student()
        self.show_exam()
        self.show_sports()


# Creating object
s1 = StudentProfile(
    "Krishna Kewat",
    21,
    "12th Science",
    88,
    "A",
    "Cricket",
    "District Level"
)

# Display output
s1.show_profile()