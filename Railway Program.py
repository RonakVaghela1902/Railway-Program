import random, time

totalSeats = 10
availableSeats = [i for i in range(1, (totalSeats + 1))]
bookedSeats = []

class Train:
    def __init__(self, name, fare, seats, booked):
        self.name = name
        self.fare = fare
        self.seats = seats
        self.booked = booked

    def getStatus(self):
        print("**********************************")
        print(f"The name of train is {self.name}.")
        print(f"The seats available in the train are \n{self.seats}.")
        print(f"The seats booked in the train are \n{self.booked}.")
        print("**********************************")

    def getFareInfo(self):
        print("**********************************")
        print(f"The price of ticket is Rs.{self.fare}.")
        print("**********************************")

    def bookTicket(self):
        if len(availableSeats) > 0:
            seatNo = random.choice(availableSeats)
            availableSeats.remove(seatNo)
            bookedSeats.append(seatNo)
            print(f"Your tickt is booked.Your seat number is {seatNo}")
        else:
            print("Sorry the train is full.Kindly try in tatkal")

    def cancelTicket(self):
        cancelTicket = int(input("Enter seat number you want to cancel : "))
        if cancelTicket in bookedSeats:
            availableSeats.append(cancelTicket)
            print(f"Your ticket number {cancelTicket} is cancelled successfully.")
            bookedSeats.remove(cancelTicket)
        else:
            print(f"Invalid Seat Number")

ticket = Train("Rajdhani Express", 500, availableSeats, bookedSeats)

if __name__ == "__main__":
    while (True):
        welcomeMSG = '''============ Welcome to Indian Railway ============
                  Please choose an option:
                  1. Get status.
                  2. Get fair information.
                  3. Book ticket
                  4. Cancel ticket
                  5. Exit website.'''
                  
        print(welcomeMSG)
        a = input("Enter your choice : ")
        
        try:
            if int(a) == 1:
                ticket.getStatus()
            elif int(a) == 2:
                ticket.getFareInfo()
            elif int(a) == 3:
                ticket.bookTicket()
            elif int(a) == 4:
                ticket.cancelTicket()
            elif int(a) == 5:
                print("Thank you for visiting Indian Railway website. Have a great day ahead!")
                time.sleep(3)                   # adding 2 seconds time delay
                exit()
            else:
                print("Invalid Choice!")
        except Exception as e:
            print("Invalid Choice!")
