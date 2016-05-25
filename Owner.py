

class Owner:

    def __init__(self):
        self.accountValue=0     ## this could be in the inventory:Class-Attribute
        self.name = ''
        self.age = 0

    def addFunds(self, pMoney):
        self.accountValue += pMoney

    def withdrawFunds(self,pMoney):
        self.accountValue -= pMoney
        if self.accountValue <0 :
            self.accountValue = 0
        return self.accountValue
