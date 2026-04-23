'''###############output#########
Name   : Krishna Kewat
Course : Python Programming
City   : Jabalpur
##############################'''   

# Base class
class Person:
    def __init__(self, name):
        self.name = name

    def show_person(self):
        print(f"Name   : {self.name}")


# Intermediate class
class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def show_course(self):
        print(f"Course : {self.course}")


# Derived class (Multilevel inheritance)
class StudentDetails(Student):
    def __init__(self, name, course, city):
        super().__init__(name, course)
        self.city = city

    def show_details(self):
        self.show_person()
        self.show_course()
        print(f"City   : {self.city}")


# Object creation
s1 = StudentDetails("Krishna Kewat", "Python Programming", "Jabalpur")

# Display output
s1.show_details()