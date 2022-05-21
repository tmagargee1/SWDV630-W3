from Order import Order

class LocalOrder(Order):
    
    def __init__(self, fName, lName, orderItems, cashier, eatIn, numPeople):
        super().__init__(fName, lName, orderItems)
        self.cashier = cashier
        self.eatIn = eatIn
        if (eatIn):
            self.assignSeat(numPeople)

    def assignSeat(self, numPeople):
        #Pretend that dominos assigns seats
        self.seats = range(numPeople)

    def createAccount(self):
        #Do steps to create a dominos count in store
        print("Account Created")