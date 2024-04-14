
class Programmer():
    company="Google"
    def __init__(self, name, product):
        self.name=name
        self.product=product
    
    def printDetails(self):
        print(f"The name of the employee is {self.name} and is working on {self.product}.")

Sanku=Programmer("Sanku", "Youtube")
Smita=Programmer("Smita", "Google Lens")
Pancham=Programmer("Pancham", "Maps")
Piyush=Programmer("Piyush", "Youtube")

Sanku.printDetails()
Pancham.printDetails()
Piyush.printDetails()
