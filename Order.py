from datetime import datetime
from pickle import FALSE, TRUE

from Enums import PaymentMethod

class Order:
    def __init__(self, fName, lName, orderItems):
        self.customerFirstName = fName
        self.customerLastName = lName
        self.timePlaced = datetime.now()
        self.orderItems = orderItems
        self.totalCost = orderItems.getTotalCost()
        self.paid = FALSE

        
    def getEstimatedTime(self):
        #Assumes 10 minutes from makeline to cut and one minute to prepare each item
        return 10 + sum(self.orderItems.quantity)

    def processPayment(self, paymentMethod):
        if(paymentMethod == PaymentMethod.CASH):
            #Process Cash Payment
            print("Cash processed")
        elif(paymentMethod == PaymentMethod.GIFT_CERTIFICATE):
            #Process Gift Card
            print("Gift card processed")
        elif(paymentMethod == PaymentMethod.CARD):
            #Process Card
            print("Credit/debit card processed")
        else:
            raise Exception("Invalid Payment type")

        self.paid = TRUE