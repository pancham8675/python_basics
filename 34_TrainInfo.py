
class Train():
    def __init__(self, name, seats, fare):
        self.name=name
        self.seats=seats
        self.fare=fare

    def trainDetails(self):
        print(f"\n*****Train Details*****\n\n Train: {self.name}\n Seats available: {self.seats}\n Fare: {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"\nYour ticket has been successfully booked and your seat number is {self.seats}.")
            self.seats=self.seats-1
        else:
            ("\nSorry, all the seats are booked.")

a = Train("Pragati Express 11292", 354, 100)

a.trainDetails()
a.bookTicket()
a.bookTicket()
a.bookTicket()
a.bookTicket()

