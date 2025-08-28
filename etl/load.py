import pandas as pd
from pathlib import Path

PROC_DIR = Path("data/processed")
PROC_DIR.mkdir(parents=True, exist_ok=True)

def save_output(df: pd.DataFrame, fmt: str = "csv"):
    if fmt == "csv":
        df.to_csv(PROC_DIR / "air_quality_weather.csv", index=False)
    elif fmt == "parquet":
        df.to_parquet(PROC_DIR / "air_quality_weather.parquet", index=False)
    print(f"✅ Data saved to {PROC_DIR} in {fmt.upper()} format")
