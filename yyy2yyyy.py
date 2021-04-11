#!/usr/bin/env python

import sys
import pandas as pd


def main(args):
    if not args[0]:
        sys.exit(1)

    df = pd.read_csv(
        args[0],
    )
    df.drop('Unnamed: 0', axis=1, inplace=True)
    df.drop(df.filter(regex="Unnamed"),axis=1, inplace=True)

    d = df['報告日期']
    for i in range(len(df)):
        d.iloc[i]=d.iloc[i].replace(d.iloc[i][0:3], str(int(d.iloc[i][0:3]) + 1911))
    d=pd.to_datetime(d,format='%Y/%m/%d')
    #df['報告日期'] = pd.to_datetime(df['報告日期'])
    #df['報告日期'] = pd.to_datetime(df['報告日期'])
    df.to_csv(args[0])


if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
