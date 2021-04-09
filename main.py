#!/usr/bin/env python

import xlrd
import pandas as pd
import sys


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args[0]:
        sys.exit(1)
    xls = pd.ExcelFile(args[0])
    df = xls.parse(sheetname="Sheet1", index_col=None, na_values=['NA'])
    df.to_csv(sys.stdout)
