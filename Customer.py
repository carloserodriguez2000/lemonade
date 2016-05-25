import random


class Customer:

    def __init__(self):
        self.i = 0
        # self.aCustomer = None

    def greetCustomer(self, weatherRepo):
        i=0
        interestedToBuy = random.randint(True,False)              # start at 50-50 chance to buy

        if interestedToBuy :
            if weatherRepo.isStormy():
                interestedToBuy = random.choice(list((True,False,False,False))) # Reduce probability
            elif weatherRepo.isHot():
                interestedToBuy = random.choice(list((True,True,True,False)))   # Increase probability

        return interestedToBuy