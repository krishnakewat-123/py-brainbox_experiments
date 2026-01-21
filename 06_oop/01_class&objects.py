'''###### output ######
name- krishna ,  age- 21    
name- sarthak ,  age- 22
########################
'''
# Class and object without __init__ method
class Student:
    pass # this show nothing means class has not data 

s1 = Student()   # 1st object is creating.
s1.name = "krishna"
s1.age = 21

s2 = Student() # 2nd object is  creating.
s2.name = "sarthak"
s2.age = 22

print("name-",s1.name,",  age-",s1.age)
print("name-",s2.name,",  age-",s2.age)
