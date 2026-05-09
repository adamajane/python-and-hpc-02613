import sys

import pandas as pd


if __name__ == "__main__":
    path = sys.argv[1]
    chunksize = int(sys.argv[2])

    total = 0.0
    for chunk in pd.read_csv(path, chunksize=chunksize):
        total += chunk.loc[chunk["parameterId"] == "precip_past10min", "value"].sum()
    print(total)
