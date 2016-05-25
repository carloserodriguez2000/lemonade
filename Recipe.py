import Lime         from Lemon
import YellowLemon  from  Lemon

class Recipe:
    def __init__(self):
        QtyLemons = 4
        QtyWater  = 1
        QtySugar  = 2

class SourRecipe(Recipe):
        lemon = Lime()

class SweetRecipe(Recipe):
        lemon = YellowLemon()
