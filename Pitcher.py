

class Pitcher:

    def __init__(self):
        i=0
        self.capacity = 40      # 40 ounces
        self.level = 0

    def serveCup(self, quantity):
        if self.level >0:
            self.level -= 1
        else:
            print (' ERROR: pitcher empty serveCup')

        return self.level           # Caller to check if it is empty

