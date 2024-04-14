
class Employee(): #Declaring class

    def __init__(self, name, salary, subunit):  # Constructor
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Yahooo!...Employee is created")

    def getDetails(self):
        print(f"The name of the employee is {self.name}.")
        print(f"The salary of the employee is {self.salary}.")
        print(f"The company of the employee is {self.subunit}.")

    company="Google" #Declaring Attribute
    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod #Makes theb program static
    def greet():
        print("Good Morning, Sir!")

Om=Employee("Om", 100000, "Youtube")
# Om=Employee() # ---> Throws an error (missing 3 required positional arguments)

Om.getDetails()
