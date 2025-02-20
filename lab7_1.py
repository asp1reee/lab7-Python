import requests


def get_weather(city):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "ru"
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]

        print(f"Погода в {city}: {weather}")
        print(f"Температура: {temp}°C")
        print(f"Влажность: {humidity}%")
        print(f"Давление: {pressure} hPa")
    else:
        print("Ошибка")


if __name__ == "__main__":
    api_key = "cde431b99d0896388c05197ce88db36d"
    city_name = "Barcelona"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    get_weather(city_name)