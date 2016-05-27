import Weather


class WeatherReport:

    def __init__(self):
        self.weather = ''
        self.precipitation = ''
        self.temperature = ''

    def getReport(self):
        newWeather = Weather.Weather()
        self.weather = newWeather.getWeather()
        self.precipitation = newWeather.getPrecipitation()
        self.temperature = newWeather.getTemperature()
        del newWeather

    def isStormy(self):

        if self.weather == 'THUNDER STORM':
            return True
        if self.weather == 'CLOUDY' and self.precipitation == 'RAINY':
            return True
        return False

    def isHot(self):
        if self.temperature > 75 :
            return True
        else :
            return False

    def isCold(self):
        if self.temperature < 60 :
            return True
        if self.precipitation == 'SNOW' :
            return True

        return False
