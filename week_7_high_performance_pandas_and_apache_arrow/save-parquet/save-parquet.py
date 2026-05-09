import os
import sys

import pandas as pd


if __name__ == "__main__":
    csv_path = sys.argv[1]
    base, _ = os.path.splitext(csv_path)
    if base.endswith(".csv"):
        base = base[:-4]
    out_path = base + ".parquet"

    df = pd.read_csv(csv_path)
    df.to_parquet(out_path)
    print(out_path)
