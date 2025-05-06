import os
import requests

API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
PARAMS = {
    "key": API_KEY,
    "q": "Paris",
    "aqi": "no"
}


def get_weather() -> None:

    response = requests.get(URL, params=PARAMS)
    data = response.json()

    if response.status_code == 200:
        city = data["location"]["name"]
        country = data["location"]["country"]
        time = data["location"]["localtime"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"{city}/{country} {time} "
              f"Weather: {temperature} Celsius, {condition}")

    else:
        error = data["error"]["message"]

        print(f"Status code: {response.status_code}. Error: {error}")


if __name__ == "__main__":
    get_weather()
