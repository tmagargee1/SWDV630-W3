from pickle import TRUE
from Enums import PaymentMethod
from Order import Order
from DeliveryOrder import DeliveryOrder
from CarsideOrder import CarsideOrder
from LocalOrder import LocalOrder
from OrderItems import OrderItems

def main():
    print("Creating Delivery")
    delivery = DeliveryOrder("John", "Doe", OrderItems([1, 2], [1, 1], [5, 10]), "123 tree Rd")
    print(delivery)
    print()
    delivery.assignDriver()
    delivery.processPayment(PaymentMethod(1))
    print(delivery)
    print()

    print("\nCreating Carside")
    carside = CarsideOrder("Jane", "Doe", OrderItems([2, 3], [3, 2], [10, 7]), "Honda", "Blue")
    print(carside)
    print()
    carside.assignCarrier()
    carside.processPayment(PaymentMethod(2))
    print(carside)
    print()

    print("\nCreating Local")
    local = LocalOrder("John", "Smith", OrderItems([1, 2, 3], [3, 2, 1], [5, 6, 7]), "Adam", True, 5)
    print(local)
    print()
    local.processPayment(PaymentMethod(3))
    local.createAccount()
    print(local)

main()
