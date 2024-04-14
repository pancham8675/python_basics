
class Employee(): #Declaring class
    company="Google" #Declaring Attribute
    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod #Makes theb program static
    def greet():
        print("Good Morning, Sir!")

Om=Employee() #Object

Om.salary=100000

Om.getSalary("Thanks!") #Employee.getSalary(Om)
