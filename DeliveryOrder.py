from Order import Order

class DeliveryOrder(Order):
    
    def __init__(self, fName, lName, orderItems, address):
        super().__init__(fName, lName, orderItems)
        self.address = address
        self.driver = "None"

    def assignDriver(self):
        #Get next driver available 
        self.driver = "Person" #Update in future

    def getEstimatedTime(self):
        return super().getEstimatedTime() + self.getTimeToAddress()

    def getTimeToAddress(self):
        #Find how long of a drive self.address is from store
        return 10