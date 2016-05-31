import Lemon


class Recipe:
    def __init__(self):
        self.QtyLemons = 4
        self.QtyWater  = 1
        self.QtySugar  = 2

class SourRecipe(Recipe):
        lemon = Lemon.Lemon()

class SweetRecipe(Recipe):
        lemon = Lemon.Lemon()
