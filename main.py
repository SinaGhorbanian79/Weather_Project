import requests
import json

apiKey = "1bcff021a86229cf441db3cfed0fdf88"


class GeoApi:
    def __init__(self, city, country):
        self.city = city
        self.country = country
        self.lat = None
        self.lon = None

    def getCoordinates(self):
        geoUrl = "http://api.openweathermap.org/geo/1.0/direct"
        geoParam = {"q": f"{self.city}, {self.country}", "appid": apiKey}
        response = requests.get(geoUrl, params=geoParam)
        response.raise_for_status()
        geo_data = response.json()
        if geo_data:
            self.lat = geo_data[0]["lat"]
            self.lon = geo_data[0]["lon"]


class WeatherApi(GeoApi):
    def __init__(self, city, country):
        super().__init__(city, country)
        self.weatherdata = None

    def getWeatherInfo(self):
        self.getCoordinates()
        if self.lat is not None and self.lon is not None:
            weatherUrl = "https://api.openweathermap.org/data/2.5/weather"
            weatherParam = {
                "lat": self.lat,
                "lon": self.lon,
                "units": "metric",
                "appid": apiKey,
            }
            response = requests.get(weatherUrl, params=weatherParam)
            response.raise_for_status()
            self.weatherdata = response.json()


class ForecastApi(GeoApi):
    def __init__(self, city, country):
        super().__init__(city, country)
        self.forecast = None

    def getForecastInfo(self):
        self.getCoordinates()
        if self.lat is not None and self.lon is not None:
            forecastUrl = "https://api.openweathermap.org/data/2.5/forecast"
            forecastParam = {
                "lat": self.lat,
                "lon": self.lon,
                "units": "metric",
                "appid": apiKey,
            }
            response = requests.get(forecastUrl, params=forecastParam)
            response.raise_for_status()
            self.forecastData = response.json()


class WeatherApp:
    def __init__(self):
        self.city = input("Please Enter Your City:\n")
        self.country = input("Please Enter Your Country:\n")
        self.option = input("Would You Like To See 5 Day Forecast As Well?[Y/n]\n")

    def run(self):
        weatherinfo = WeatherApi(self.city, self.country)
        weatherinfo.getWeatherInfo()
        print(weatherinfo.weatherdata)

        if (
            self.option.lower() == "yes"
            or not self.option
            or self.option.lower() == "y"
        ):
            forecastinfo = ForecastApi(self.city, self.country)
            forecastinfo.getForecastInfo()
            print(forecastinfo.forecastData)


if __name__ == "__main__":
    runApp = WeatherApp()
    runApp.run()
