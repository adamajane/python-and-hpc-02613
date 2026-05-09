import pandas as pd


def reduce_dmi_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if "parameterId" in df.columns:
        df["parameterId"] = df["parameterId"].astype("category")
    if "stationId" in df.columns:
        df["stationId"] = df["stationId"].astype("category")
    if "value" in df.columns:
        df["value"] = df["value"].astype("float32")
    if "coordsx" in df.columns:
        df["coordsx"] = df["coordsx"].astype("float32")
    if "coordsy" in df.columns:
        df["coordsy"] = df["coordsy"].astype("float32")
    for col in ("created", "observed"):
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")
    return df


if __name__ == "__main__":
    path = "/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip"
    df = pd.read_csv(path)
    before = df.memory_usage(deep=True).sum() / 1024**2
    df2 = reduce_dmi_df(df)
    after = df2.memory_usage(deep=True).sum() / 1024**2
    print(f"Before: {before:.2f} MB")
    print(f"After:  {after:.2f} MB")
    print(f"Reduction: {(1 - after / before) * 100:.1f}%")
