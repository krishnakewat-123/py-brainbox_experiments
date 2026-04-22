'''######### output ##############
#This is method1 from class A
This is method2 from class B
##############################'''
class A:
    def method1(self):
        print("This is method1 from class A")


class B(A):
    def method2(self):
        print("This is method2 from class B")


b = B()
b.method1()
b.method2()