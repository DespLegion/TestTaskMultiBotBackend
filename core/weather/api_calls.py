import conf
import requests


class SyncWeatherAPI:
    def __init__(self):
        self.base_url = f"https://api.api-ninjas.com/v1/weather"
        self.headers = {
            'X-Api-Key': conf.API_N_TOKEN,
            'Content-Type': 'application/json'
        }

    def get_weather(self, location: dict):

        res = requests.get(url=self.base_url, headers=self.headers, params=location)
        if res.status_code == 200:
            json_res = res.json()
            res_weather = {
                "cur_temp": json_res["temp"],
                "temp_feels_like": json_res["feels_like"],
                "cloud": json_res["cloud_pct"],
                "wind_speed": json_res["wind_speed"],
            }
            return res_weather
        else:
            return "Some error"

    @staticmethod
    def get_city_name(lat: float, lon: float):
        url = f"https://nominatim.openstreetmap.org/reverse"
        headers = {
            'Content-Type': 'application/json'
        }
        params = {
            "format": "json",
            "lat": lat,
            "lon": lon
        }
        res = requests.get(url=url, headers=headers, params=params)

        if res.status_code == 200:
            json_res = res.json()
            return json_res["address"]["city"]
        else:
            return "Unknown"
