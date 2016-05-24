from datetime import date

class Lemon:
    def __init__(self):
        self.purchaseDate= date.today()
        self.expiration= self.purchaseDate + 2      # lemons expire in two day.
        self.size = 0
        self.type = 0
        self.calories = 5
        self.stored = True                          # stored lemons are available. Otherwise it expired or was used

    def Buy(self):
        self.i=0

    def Use(self):
        self.i=0
        # i

    def Store(self):
        self.stored = True

class Lime(Lemon):
    def __init__(self):
        self.i=0
        self.sourLevel  = 5
        slef.sweetLevel = 1

class YellowLemon(Lemon):
    def __init__(self):
        self.i=0
        self.sourLevel = 2
        self.sweetLevel = 5
