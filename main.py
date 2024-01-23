import requests
import json

apiKey = "1bcff021a86229cf441db3cfed0fdf88"


class main:
    def __init__(self, city, country):
        self.city = city
        self.country = country

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


result = main("shiraz", "iran")
result.geoCaller()
result.manipulator()
result.weatherCaller()

print(result.response.text)


# class currentWeather:
#     def __init__(self, lat, lon):
#         self.lat = lat
#         self.lon = lon

#     self.response = geoCoding.apiCaller


# geoCoder = geoCoding("mashhad", "iran")
# geoCoder.apiCaller()
# geoCoder.manipulator()
# weatherDisplayer = currentWeather(geoCoder.lat, geoCoder.lon)

# params={"q": self.city + "," + self.country, "appid": apiKey}
