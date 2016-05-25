import Weather


class WeatherReport:

    def __init__(self):
        self.weather = None
        self.precipitation = None
        self.temperature = None

    def getReport(self):
        newWeather = Weather.Weather()
        self.weather = newWeather.getWeather()
        self.precipitation = newWeather.getPrecipitation()
        self.temperature = newWeather.getTemperature()
        del newWeather

