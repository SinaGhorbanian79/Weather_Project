import requests
import json


class geoCoding:
    def __init__(self, city, country):
        self.city = city
        self.country = country
        self.apiCaller()

    def apiCaller(self):
        self.url = "http://api.openweathermap.org/geo/1.0/direct"
        self.apiKey = "1bcff021a86229cf441db3cfed0fdf88"
        self.response = requests.get(
            self.url, params={"q": self.city + "," + self.country, "appid": self.apiKey}
        )
        self.manipulator()

    def manipulator(self):
        self.jsonResponse = self.response.json()
        self.lat = self.jsonResponse[0]["lat"]
        self.lon = self.jsonResponse[0]["lon"]


gc = geoCoding("mashhad", "iran")
print(f"{gc.lat} {gc.lon}")
