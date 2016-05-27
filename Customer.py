import random
import WeatherReport


class Customer:

    def __init__(self):
        self.i = 0
        self numberOfCustomers

    def isInterested(self, weatherRepo):
        i=0
        interestedToBuy = random.choice(list((True,False)))              # start at 50-50 chance to buy

        if interestedToBuy == True :
            if weatherRepo.isStormy():
                interestedToBuy = random.choice(list((True,False,False,False))) # Reduce probability
            elif weatherRepo.isHot():
                interestedToBuy = random.choice(list((True,True,True,False)))   # Increase probability
            elif weatherRepo.isCold() :
                interestedToBuy = random.choice(list((True,False,False,False))) # Reduce probability

        return interestedToBuy