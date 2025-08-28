import argparse
from etl import ingest, transform, load

def run_pipeline(fmt: str = "csv"):
    # Step 1: Ingest raw data
    air_quality, weather = ingest.fetch_data()

    # Step 2: Transform (join + clean)
    merged = transform.join_datasets(air_quality, weather)

    # Step 3: Load to processed/
    load.save_output(merged, fmt=fmt)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ETL Pipeline Runner")
    parser.add_argument("--fmt", default="csv", choices=["csv", "parquet"],
                        help="Output format (csv or parquet)")
    args = parser.parse_args()

    run_pipeline(fmt=args.fmt)
