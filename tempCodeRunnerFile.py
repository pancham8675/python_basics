class Employee(): #Declaring class
    company="Google" #Declaring Attribute
    salary="100"

Om=Employee() #Object
Raj=Employee()
Ruchita=Employee()


Ruchita.salary="300" #Instance attribute

print(Raj.company)

Employee.company="Youtube"

print(Raj.company)
print(Om.salary)
print(Ruchita.salary)