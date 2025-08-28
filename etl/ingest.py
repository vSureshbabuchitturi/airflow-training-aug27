import requests
import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

def fetch_air_quality():
    url = "https://api.waqi.info/feed/hyderabad/?token=demo"
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()

    if data["status"] != "ok":
        raise ValueError("WAQI API returned error")

    iaqi = data["data"]["iaqi"]

    record = {
        "datetime": data["data"]["time"]["iso"],
        "pm25": iaqi.get("pm25", {}).get("v"),
        "pm10": iaqi.get("pm10", {}).get("v"),
        "o3": iaqi.get("o3", {}).get("v"),
        "no2": iaqi.get("no2", {}).get("v"),
        "so2": iaqi.get("so2", {}).get("v"),
        "co": iaqi.get("co", {}).get("v")
    }

    df = pd.DataFrame([record])
    df.to_csv(RAW_DIR / "air_quality.csv", index=False)
    return df


def fetch_weather():
    url = (
        "https://api.open-meteo.com/v1/forecast?"
        "latitude=17.3850&longitude=78.4867&hourly=temperature_2m,relative_humidity_2m"
    )
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()

    weather_df = pd.DataFrame({
        "datetime": data["hourly"]["time"],
        "temperature": data["hourly"]["temperature_2m"],
        "humidity": data["hourly"]["relative_humidity_2m"]
    })
    weather_df.to_csv(RAW_DIR / "weather.csv", index=False)
    return weather_df


def fetch_data():
    air_quality = fetch_air_quality()
    weather = fetch_weather()
    return air_quality, weather
