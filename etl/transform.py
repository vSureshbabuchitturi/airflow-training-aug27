import pandas as pd

def join_datasets(air_quality: pd.DataFrame, weather: pd.DataFrame) -> pd.DataFrame:
    # Simplify datetime formats
    weather["datetime"] = pd.to_datetime(weather["datetime"])

    # Fake datetime column in air_quality (for demo)
    air_quality["datetime"] = pd.date_range("2025-01-01", periods=len(air_quality), freq="H")

    merged = pd.merge_asof(
        air_quality.sort_values("datetime"),
        weather.sort_values("datetime"),
        on="datetime"
    )

    # Drop duplicates, fill missing values
    merged = merged.drop_duplicates().fillna(method="ffill")
    return merged
