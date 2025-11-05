# Can you change the self-parameter inside a class to something else (say "harry").Try changing self to "slf" or "harry" and see the effects.


# Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

from random import randint

class Train:
    
    def __init__(slf, trainNo):
         slf.trainNo = trainNo

    def book(harry, fro, to):
        print(f"Ticket is booked in train no: {harry.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")
    
    def getFare(self,  fro, to):
          print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")

t = Train(12399)
t.book("Bharatpur", "Delhi")
t.getStatus()
t.getFare("Bharatpur", "Delhi")

