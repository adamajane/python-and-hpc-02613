from pyarrow import csv


def pyarrow_load(path):
    table = csv.read_csv(path)
    return table.to_pandas()


if __name__ == "__main__":
    from time import perf_counter

    path = "/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip"
    t0 = perf_counter()
    df = pyarrow_load(path)
    t1 = perf_counter()
    print(f"Loaded + converted in {t1 - t0:.3f}s")
    print(f"DataFrame: {len(df)} rows, "
          f"{df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
