'''######### output ##############
Employee: Krishna
Salary: ₹50000
Role: Software Engineer
##############################'''
class Employee:
    def __init__(self, name, salary):
        self.name = name        # stores employee name
        self.salary = salary    # stores salary

    def show_details(self):
        print(f"Employee: {self.name}")
        print(f"Salary: ₹{self.salary}")


class Manager(Employee):
    def show_role(self):
        print("Role: Software Engineer")   # role added


# creating object
m = Manager("Krishna", 50000)

m.show_details()   # parent method
m.show_role()      # child method