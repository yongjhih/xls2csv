#!/usr/bin/env python

import sys
import xlrd
import csv


def main(args):
    if not args[0]:
        sys.exit(1)
    book = xlrd.open_workbook(args[0])
    sh = book.sheet_by_index(0)
    csv_writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL)
    for i in range(sh.nrows):
        csv_writer.writerow(sh.row_values(i))


if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
