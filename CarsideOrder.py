from Order import Order

class CarsideOrder(Order):
    
    def __init__(self, fName, lName, orderItems, carMake, carColor):
        super().__init__(fName, lName, orderItems)
        self.carMake = carMake
        self.carColor = carColor
        self.carrier = "None"

    def assignCarrier(self):
        #Get next Insider available 
        self.driver = "Person" #Update in future

    def getEstimatedTime(self):
        #Carside orders are given 2 minutes for a dominos member to deliver
        return super().getEstimatedTime() + 2

