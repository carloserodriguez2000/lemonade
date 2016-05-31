import Inventory
import Sales
import Recipe
import csv

class gameRecords:

    def __init__(self):
        I=0

class Owner:

    def __init__(self):
        # self.accountValue=0     ## this could be in the inventory:Class-Attribute
        self.name = ''
        self.age = 0
        self.inventory = Inventory.Inventory()
        self.daySales = Sales.Sales()

    def addFunds(self, pMoney):
        self.inventory.addCash(pMoney)

    def withdrawFunds(self,pMoney):
        self.inventory.takeCash(pMoney)
        cashOnHand = self.inventory.checkBalance()
        if cashOnHand <0 :
            print('ERROR. negative Balance')
        return cashOnHand

    def inputOwnerInfo(self):
        name = input('Please enter your name : ')
        self.name = name.lower()
        age = input('Please enter your age: ')
        self.age = age

    def findOwnerFile(self, name):

        # open file. Check for existence of file.
        # Loop until name is found
                    # if found then load all cash and inventory
                    # else return -1
        balance = -1
        fieldNames = ['Name', 'CashQty',
                     'LemQty', 'LemDate', 'LemPrice',
                     'IceQty','IceDate', 'IcePrice',
                     'SugarQty', 'SugarPrice',
                     'CupsQty', 'CupPrice',
                     'GameStart','GameEnd']
        with open('GameRec.csv', 'r',) as csvfile:
            reader = csv.DictReader(csvfile, fieldNames)
            for row in reader:
                if (name == row['Name']):
                    print ('FOUND')
                    self.inventory.loadOldInventory(row)
                    balance = self.inventory.cash
                    break
        return balance

    def printInventory(self):
        print('             Cash       = %f' % (self.inventory.cash))
        print('             Lemons     = %i' % (len(self.inventory.lemons)))
        print('             Cups       = %i' % (len(self.inventory.cups)))
        print('             Sugar      = %i' % (len(self.inventory.sugar)))
        print('             Ice Cubes  = %i' % (len(self.inventory.iceCubes)))

    def enoughInventory(self):
        return self.inventory.enoughInventory()

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
            funds = 20
            self.addFunds(funds)  # if the owner has zero Balance
            self.inventory.addCash(funds)
        else:
            print('Welcome back %s :' %(self.name))
            print('Your account Balance is $%s' %(self.inventory.cash))
            print('You have the following inventory:')
            self.printInventory()
            return

    def fillCup(self, aCup, aPitcher):
        if aPitcher.level <= 0:
            self.inventory.fillPitcher()
        aPitcher.serveCup(1)  # serve one cup.
        aCup.full = True

    def giveFullCup(self,aCup):
        if aCup.full == True:
            self.daySales.storeSale('today','Nice Person')
            del aCup                    # destroy memory object.
        else :
            print('        ERROR... giving empty cup')




