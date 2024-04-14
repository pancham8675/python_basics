
class Person():
    country="India"

    def breathe(self):
        print("I am breathing...")

class Employee(Person):
    company="Honda"

    def salary(self):
        print(f"The salary of the eployee is {self.salary}")

    def breathe(self):
        super().breathe()
        print("I am an employee and I am luckily breathing...")

class Programmer(Employee):
    company="Fiverr"

    def salary(self):
        print("No salary to the programmer")

    def breathe(self):
        super().breathe()
        print("I am an programmer and I am breathing++")

p=Person()
p.breathe()

e=Employee()
e.breathe()

pr=Programmer()
pr.breathe()

