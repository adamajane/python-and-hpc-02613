from pyarrow import csv


def pyarrow_load(path):
    return csv.read_csv(path)


if __name__ == "__main__":
    from time import perf_counter

    path = "/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip"
    t0 = perf_counter()
    table = pyarrow_load(path)
    t1 = perf_counter()
    print(f"Loaded with PyArrow in {t1 - t0:.3f}s")
    print(f"Table size: {table.nbytes / 1024**2:.2f} MB, rows: {table.num_rows}")
