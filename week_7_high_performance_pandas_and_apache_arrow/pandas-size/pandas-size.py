import pandas as pd


def df_memsize(df: pd.DataFrame) -> int:
    return df.memory_usage(deep=True).sum()


# df = pd.read_csv("../2023_01.csv")
df = pd.read_csv("/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip")
size = df_memsize(df)
print(f"DataFrame memory usage: {size} bytes ({size / 1024**2:.2f} MB)")
