import random

class Weather:


    def __init__(self):
        self.weatherList = ('SUNNY', 'PARTLY CLOUDY', 'CLOUDY', 'THUNDER STORM')
        self.precipitationList = ('RAINY', 'SNOW',)
        self.temperatureList = list(range(30,110,5))

    def getWeather(self):
        value = random.choice(self.weatherList)
        return value

    def getPrecipitation(self):
        value = random.choice(self.precipitationList)
        return value

    def getTemperature(self):
        value = random.choice(self.temperatureList)
        return value
    