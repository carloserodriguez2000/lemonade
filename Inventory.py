import Cup
import Lemon
import IceCube
import Pitcher
import Sugar

class Inventory:

    def __init__(self):
        self.lemons   = []             #???? create instance of lemon class. Get quantity from game setup.
        self.iceCubes = []           # instance of icecube
        self.cups     = [] # instance of Class Cups.
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
        i=0
            # if lemon expired. Delete it.
            # if no lemons left UPPS
            # if not enough Lemons left UPPS
        # subtract cash from each transaction

        if len(self.lemons) < 1 :               # add logic to handle minimun number of lemons.
            # HANDLE ERROR CONDITION
            # append a bunch using a loop OR
            self.lemons.append(Lemon.Lemon())  # add a cup to the list of cups

        useLemon = Lemon.Lemon()
        for useLemon in self.lemons:
            if useLemon.isExpired()

        self.lemons.remove(self,quantity)

    def TakeIce(self, quantity):
        i=0
        # if ice expired. Delete it.
        # if no ice left UPPS
        # if not ice  left UPPS
        # if ice Melting, do some fancy thing


    def TakeCup(self, quantity):
        i = 0
        # if cup expired. Delete it.
        # if no cup left UPPS
        # if not cup  left UPPS
        #