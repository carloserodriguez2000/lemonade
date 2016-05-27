import random
import Cup
import Lemon
import IceCube
import Pitcher
import Sugar
import Recipe


class Inventory:
    def __init__(self):
        self.lemons = []  # ???? create instance of lemon class. Get quantity from game setup.
        self.iceCubes = []  # instance of icecube
        self.cups = []  # instance of Class Cups.
        self.sugar = []
        self.pitcher = Pitcher.Pitcher()  # create instance of a pitcher
        self.cash = 0  # Cash on hand to use for purchasing supplies
        self.maxCups = 200
        self.sugarPrice = 0.25  # 0.25 per cup of sugar
        self.icePrice = 0.01  # 0.01 per cube
        self.cupPrice = 0.05  # 0.05 per each cup
        self.lemonPrice = 0.25  # 0.25 per each lemon
        self.maxCubes = 500
        self.maxLemons = 100
        self.maxSugar = 100

    def addCash(self, quantity):
        self.cash += quantity

    def takeCash(self, quantity):
        self.cash -= quantity
        if self.cash < 0:
            print('\n           ERROR   takeCash\n')

    def checkBalance(self):
        return self.cash

    def enoughInventory(self):
        if len(self.lemons) == 0 or \
                        len(self.cups)     == 0 or\
                        len(self.sugar)    == 0 or \
                        len(self.iceCubes) == 0:
            return False

    def addLemons(self, quantity, pPrice):  # Buy lemons, Subtract cash from
        if (quantity + len(self.lemons)) > self.maxLemons:
            i = 0
            # HANDLE ERROR CONDITION
            # append a bunch using a loop OR
        else:
            for index in range(0, quantity):  # self.lemons.extend( quantity*[Lemon.Lemon()])
                newLemon = Lemon.Lemon()
                newLemon.price = pPrice
                self.lemons.append(newLemon)

            self.takeCash(quantity * pPrice)

    def addIcubes(self, quantity, pPrice):
        if (quantity + len(self.iceCubes)) > self.maxCubes:
            i = 0
            # HANDLE ERROR CONDITION
        else:
            ##self.iceCubes.extend(quantity[IceCube.IceCube(20)])    # add a icecubes to the list of cubes. 20 DEG colds
            for index in range(0, quantity):  # self.lemons.extend( quantity*[Lemon.Lemon()])
                newIceCube = IceCube.IceCube(20)
                newIceCube.price = pPrice
                self.iceCubes.append(newIceCube)

            self.takeCash(quantity * pPrice)

    def addCups(self, quantity, pPrice):
        if (quantity + len(self.cups)) > self.maxCups:
            i = 0
            # HANDLE ERROR CONDITION
        else:
            ##self.cups.extend(quantity*[Cup.Cup()])    # add  cups to the list of cups
            for index in range(0, quantity):  # self.lemons.extend( quantity*[Lemon.Lemon()])
                newcup = Cup.Cup()
                newcup.price = pPrice
                self.cups.append(newcup)

            self.takeCash(quantity * pPrice)

    def addSugar(self, quantity, pPrice):
        if (quantity + len(self.sugar)) > self.maxSugar:
            # HANDLE ERROR CONDITION
            i = 0
        else:
            # self.sugar.extend(quantity*[Sugar.Sugar()])  # add quantity sugar objects to the list
            for index in range(0, quantity):  # self.lemons.extend( quantity*[Lemon.Lemon()])
                newSugar = Sugar.Sugar()
                newSugar.price = pPrice
                self.sugar.append(newSugar)

            self.takeCash(quantity * pPrice)

    def takeSugar(self, quantity):

        numSugarsLeft = len(self.sugar)
        gotSugars = 0  # Flag to indicate we got the "quantity" asked.
        while numSugarsLeft > 0 and gotSugars < quantity:
            gotSugars += 1
            self.cups.pop()  # remove cup from inventory.
            numSugarsLeft = len(self.sugar)
        return gotSugars  # contains "0 >= gotSugars <= quantity"

    def takeLemons(self, quantity):  # take lemons out of inventory to make lemonade
        numLemonsLeft = len(self.lemons)
        gotLemons = 0  # Flag to indicate we got the "quantity" asked.
        while numLemonsLeft > 0 and gotLemons < quantity:
            randomLemon = random.randrange(0,
                                           numLemonsLeft)  # also random.choice(lemons), or random.choice(list(range(10)))
            thisLemon = self.lemons[randomLemon]
            if thisLemon.isExpired == False:
                gotLemons += 1
            self.lemons.pop(randomLemon)  # remove lemon from inventory. found a good one or removed a bad one.
            numLemonsLeft = len(self.lemons)
        return gotLemons  # contains "0 >= gotLemons <= quantity"

    def takeIce(self, quantity):
        numIceCubesLeft = len(self.iceCubes)
        gotIcecubes = 0  # Flag to indicate we got the "quantity" asked.
        while numIceCubesLeft > 0 and gotIcecubes < quantity:
            randomIceCube = random.randrange(0,
                                             numIceCubesLeft)  # also random.choice(lemons), or random.choice(list(range(10)))
            thisIceCube = self.iceCubes[randomIceCube]
            if thisIceCube.isExpired == False:
                gotIcecubes += 1
                self.iceCubes.pop(randomIceCube)  # remove lemon from inventory. found a good one or removed a bad one.
            numIceCubesLeft = len(self.iceCubes)
        return gotIcecubes  # contains "0 >= gotLemons <= quantity"

    def takeWater(self, quantity):
        return quantity

    def takeCup(self, quantity):
        numCupsLeft = len(self.iceCubes)
        gotCups = 0  # Flag to indicate we got the "quantity" asked.
        cupObject = []
        while numCupsLeft > 0 and gotCups < quantity:
            gotCups += 1
            cupObject = self.cups.pop()  # remove cup from inventory.
            numCupsLeft = len(self.cups)
        return cupObject

    def fillPitcher(self, recipe):
        i = 0
        # refill the pitcher when it is empty
        # pitcher to contain Cups? or ounces.
        # Uses lemons, sugar, water.
        # subtract from inventory
        # Check that there are enough lemons
        # ex. if recipe.lemons > len(self.lemons))  Then error. not enough lemons.
        if self.pitcher.level != 0:
            # error handling
            i = 0
        else:
            self.takeLemons(recipe.QtyLemons)
            self.takeSugar(recipe.QtySugar)
            self.takeWater(recipe.QtyWater)
            self.pitcher.level = self.pitcher.capacity  # set the pitcher to full capacity
