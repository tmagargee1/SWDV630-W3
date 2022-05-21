class OrderItems: 
    def __init__(self, orderIds, quantity, prices):
        self.orderIds = orderIds
        self.quantity = quantity
        self.prices = prices

    def getTotalCost(self):
        total = 0
        for i, quant in enumerate(self.quantity):
            total += quant * self.prices[i]
        return total