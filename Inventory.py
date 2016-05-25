import random
import Cup
import Lemon
import IceCube
import Pitcher
import Sugar

class Inventory:

    def __init__(self):
        self.lemons   = []             #???? create instance of lemon class. Get quantity from game setup.
        self.iceCubes = []              # instance of icecube
        self.cups     = []              # instance of Class Cups.
        self.sugar    = []
        self.pitcher  = Pitcher.Pitcher()     # create instance of a pitcher
        self.cash     =0              # Cash on hand to use for purchasing supplies
        self.maxCups    = 200
        self.maxCubes   = 500
        self.maxLemons  = 100
        self.maxSugar   = 100

    def addLemons(self, quantity):                          #Buy lemons, Subtract cash from
        if (quantity + len(self.lemons)) > self.maxLemons:
            i = 0
                    # HANDLE ERROR CONDITION
                    # append a bunch using a loop OR
        self.lemons.append( Lemon.Lemon())  # add a cup to the list of cups

    def addIcubes(self, quantity):
        if (quantity+len(self.iceCubes))  > self.maxCubes:
            i = 0
            # HANDLE ERROR CONDITION
                    # append a bunch using a loop OR
        self.iceCubes.append(IceCube.IceCube(20))    # add a cup to the list of cubes. 20 DEG colds

    def addCups(self, quantity):
        if ( quantity+len(self.cups))  > self.maxCups:
            i = 0
                                            # HANDLE ERROR CONDITION
        # append a bunch using a loop OR
        self.cups.append(Cup.Cup())    # add a cup to the list of cups

    def addSugar(self,quantity):
        if ( quantity+len(self.sugar)) > self.maxCups:
            # HANDLE ERROR CONDITION
                    # append a bunch using a loop OR
            self.sugar.append(Sugar.Sugar())  # add a cup to the list of cups

    def fillPitcher(self):      # refill the pitcher when it is empty
                                # pitcher to contain Cups? or ounces.
                                # Uses lemons, sugar, water.
                                # subtract from inventory
        # Check that there are enough lemons
        # ex. if recipe.lemons > len(self.lemons))  Then error. not enough lemons.
        if self.pitcher.capacity != 0:
            # error handling
            i = 0
        else:
            self.pitcher.level = self.pitcher.capacity      # Fill the pitcher

    def TakeLemons(self, quantity):  # take lemons out of inventory to make lemonade
        numLemonsLeft = len (self.lemons)
        gotLemons     = 0                                       # Flag to indicate we got the "quantity" asked.
        while numLemonsLeft >0 and gotLemons < quantity :
            randomLemon = random.randrange(0,numLemonsLeft)     # also random.choice(lemons), or random.choice(list(range(10)))
            thisLemon = self.lemons[randomLemon]
            if thisLemon.isExpired == False
                gotLemons +=1
            self.lemons.pop(randomLemon)                    # remove lemon from inventory. found a good one or removed a bad one.
            numLemonsLeft = len(self.lemons)
        return gotLemons                                    # contains "0 >= gotLemons <= quantity"


    def TakeIce(self, quantity):
        numIceCubesLeft = len (self.iceCubes)
        gotIcecubes     = 0                                         # Flag to indicate we got the "quantity" asked.
        while numIceCubesLeft >0 and gotIcecubes < quantity :
            randomIceCube = random.randrange(0,numIceCubesLeft)     # also random.choice(lemons), or random.choice(list(range(10)))
            thisIceCube = self.iceCubes[randomIceCube]
            if thisIceCube.isExpired == False
                gotIcecubes +=1
                self.iceCubes.pop(randomIceCube)                    # remove lemon from inventory. found a good one or removed a bad one.
            numIceCubesLeft = len(self.iceCubes)
        return gotLemons                                            # contains "0 >= gotLemons <= quantity"

    def TakeCup(self, quantity):
        numCupsLeft = len(self.iceCubes)
        gotCups = 0  # Flag to indicate we got the "quantity" asked.
        while numCupsLeft > 0 and gotCups < quantity:
            gotCups += 1
            self.cups.pop()  # remove cup from inventory.
            numCupsLeft = len(self.cups)
        return gotCups  # contains "0 >= gotLemons <= quantity"
