# Multiple Inheritance

class Employee():
    company="Visa"
    ecode=102

class Freelancer():
    company="Fiverr"
    level=2

    def upgradeLevel(self):
        self.level=self.level+1

class Programmer(Employee, Freelancer):
    name="Rohit"

p=Programmer()
p.upgradeLevel()
print(p.level)


