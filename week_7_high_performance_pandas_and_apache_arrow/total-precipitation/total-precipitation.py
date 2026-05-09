import sys

import pandas as pd


if __name__ == "__main__":
    csv_path = sys.argv[1]
    df = pd.read_csv(csv_path)
    total = df.loc[df["parameterId"] == "precip_past10min", "value"].sum()
    print(total)
