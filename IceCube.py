from datetime import datetime

class IceCube:

    def __init__(self, pTemperature):
        self.Temperature = pTemperature    # degrees Fahrenheit
        self.MeltRate    = 1          # maybe based on day-temperature. ex. %reduction every hour
        self.birth       =  datetime.date()
        self.lifeSpan    = 0
        self.prize = 1.0                        # dollars

        if (pDayTemperature > 80):
            self.lifeSpan = 6            # hours left before ice turns to water.
        else:
            self.lifeSpan = 9


def isExpired(self):
    if self.purchaseDate - date.today() > 2:
        # ice  is melted
        return False
    else:
        return True

