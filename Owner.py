import Inventory

class Owner:

    def __init__(self):
        self.accountValue=0     ## this could be in the inventory:Class-Attribute
        self.name = ''
        self.age = 0
        self.inventory = Inventory.Inventory()

    def addFunds(self, pMoney):
        self.accountValue += pMoney

    def withdrawFunds(self,pMoney):
        self.accountValue -= pMoney
        if self.accountValue <0 :
            self.accountValue = 0
        return self.accountValue

    def inputOwnerInfo(self):
        name = input('Please enter your name : ')
        self.name = name
        age = input('Please enter your age: ')
        self.age = age

    def findOwnerFile(self, name):
                    # OPen file
                    # read records checking for name
                    # if name found return account balance,
                    # and load prior inventory
                    # else return -1 meaning a new Owner
        balance = -1
        return balance

    def printInventory(self):
        print('             Lemons = %i' % (len(self.inventory.lemons)))
        print('             Cups   = %i' % (len(self.inventory.cups)))
        print('             Sugar  = %i' % (len(self.inventory.sugar)))

    def loadOwner(self):                  # The inventory from the last day must be retrievable
        self.inputOwnerInfo()
        balance = self.findOwnerFile(self.name)
        if balance == -1:
            print('You are a new Lemonade stand Owner: ')       # How much Money Grandma Gave you to play?
            print('Let me start you with some money:')
            self.addFunds(20)  # New player needs money
        elif  balance == 0 :
            print('Your are BROKE! ')
            print('Let me give you more money: ')
            self.addFunds(20)  # if the owner has zero Balance
        else:
            print('Welcome back %s :' %(self.name))
            print('Your account Balance is $%s' %(self.accountValue))
            print('You have the following inventory:')
            self.printInventory()
            return
