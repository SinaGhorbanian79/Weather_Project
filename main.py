import requests
import json

apiKey = "1bcff021a86229cf441db3cfed0fdf88"


class WeatherProject:
    def __init__(self, city, country):
        self.city = city
        self.country = country
        self.lat = None
        self.lon = None

    def apiCaller(self, url, parameter):
        self.url = url
        self.parameter = parameter
        self.response = requests.get(self.url, params=self.parameter)

    def geoCaller(self):
        geoUrl = "http://api.openweathermap.org/geo/1.0/direct"
        geoParam = {"q": f"{self.city}, {self.country}", "appid": apiKey}
        self.apiCaller(geoUrl, geoParam)

    def weatherCaller(self):
        weatherUrl = "https://api.openweathermap.org/data/2.5/weather"
        weatherParam = {
            "lat": self.lat,
            "lon": self.lon,
            "units": "metric",
            "appid": apiKey,
        }
        self.apiCaller(weatherUrl, weatherParam)

    def manipulator(self):
        self.jsonResponse = self.response.json()
        self.lat = self.jsonResponse[0]["lat"]
        self.lon = self.jsonResponse[0]["lon"]


if __name__ == "__main__":
    result = WeatherProject("shiraz", "iran")
    result.geoCaller()
    result.manipulator()
    result.weatherCaller()

print(result.response.text)
