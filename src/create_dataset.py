import pandas as pd
from pathlib import Path


INPUT_FILE = Path("data/raw/shipments_master.csv")
OUTPUT_FILE = Path("data/processed/shipments_120k.csv")

ROWS_TO_KEEP = 120_000


def main():
    print("Loading dataset...")

    df = pd.read_csv(
        INPUT_FILE,
        nrows=ROWS_TO_KEEP
    )

    print(f"Rows loaded: {len(df):,}")
    print(f"Columns: {len(df.columns)}")

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("\nDataset created successfully.")
    print(f"Output: {OUTPUT_FILE}")
    print(f"Rows: {len(df):,}")


if __name__ == "__main__":
    main()