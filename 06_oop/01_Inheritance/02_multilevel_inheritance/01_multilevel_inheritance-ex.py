'''######### output ##############
Class A
Class B
Class C
##############################'''
class A:
    def method1(self):
        print("Class A")


class B(A):
    def method2(self):
        print("Class B")


class C(B):
    def method3(self):
        print("Class C")


c = C()
c.method1()
c.method2()
c.method3()