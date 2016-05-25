import random


class Customer:

    def __init__(self):
        self.i = 0
        # self.aCustomer = None

    def greetCustomer(self):
        self.i=0
        wantToBuy = random.randint(True,False)

        return wantToBuy