from datetime import datetime

class IceCube:

    def __init__(self, pDayTemperature):
        Temperature = 25    # degrees Fahrenheit
        MeltRate    = 1          # maybe based on day-temperature. ex. %reduction every hour
        birth       =  datetime.date()
        lifeSpan    = 0
        if (pDayTemperature > 80):
            lifeSpan = 6            # hours left before ice turns to water.
        else:
            lifeSpan = 9



