import sys
import pandas as pd


def yyy2yyyy(yyymmdd, i, delimiter="/"):
    parts = yyymmdd.split(delimiter)
    yyy = int(parts[0]) + (100 if (parts[0].startswith("0")) else 0)
    year = 1911 + yyy + (0 if (int(parts[0]) < 2000) else -2000)
    if year > 2100 or year < 1911:
        print(f"Invalid year: {i}: {year}: {yyymmdd}: {yyy}")
    return f"{year}-{parts[1]}-{parts[2]}"

def main(args):
    if not args[0]:
        sys.exit(1)

    print("Loading")
    df = pd.read_csv(
        args[0],
    )

    try:
        df.drop('Unnamed: 0', axis=1, inplace=True)
        df.drop(df.filter(regex="Unnamed"),axis=1, inplace=True)
    except:
        pass

    print("Processing op-date")

    d = df['手術日期']

    for i in range(len(df)):
        d.iloc[i]=yyy2yyyy(d.iloc[i], i)
    pd.to_datetime(d, format='%Y-%m-%d')

    print("Processing report-date")
    d = df['報告日期']
    for i in range(len(df)):
        d.iloc[i]=yyy2yyyy(d.iloc[i], i)
    pd.to_datetime(d, format='%Y-%m-%d')

    df.to_csv(args[0])


if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
