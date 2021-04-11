#!/usr/bin/env bash

#for f in *.xls *.xlsx; do
for f in "$@"; do
  poetry run python main.py "${f}" > "${f%.*}.csv"
done
