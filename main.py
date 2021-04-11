#!/usr/bin/env python

import sys
import pandas as pd


def main(args):
    if not args[0]:
        sys.exit(1)

    df = pd.read_excel(
        args[0],
        #engine='openpyxl',
    )
    df.to_csv(sys.stdout)


if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
