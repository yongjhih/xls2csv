#!/usr/bin/env python

import sys
import pandas as pd


def yyy2yyyy(yyymmdd, delimiter="/"):
    parts = yyymmdd.split(delimiter)
    year = int(parts[0]) + 1911 + (100 if (parts[0].startswith("0")) else 0)
    return f"{year}-{parts[1]}-{parts[2]}"

def main(args):
    if not args[0]:
        sys.exit(1)

    df = pd.read_csv(
        args[0],
    )
    df.drop('Unnamed: 0', axis=1, inplace=True)
    df.drop(df.filter(regex="Unnamed"),axis=1, inplace=True)

    d = df['手術日期']
    for i in range(len(df)):
        d.iloc[i]=yyy2yyyy(d.iloc[i])
    pd.to_datetime(d, format='%Y-%m-%d')

    d = df['報告日期']
    for i in range(len(df)):
        d.iloc[i]=yyy2yyyy(d.iloc[i])
    pd.to_datetime(d, format='%Y-%m-%d')

    df.to_csv(args[0])


if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
