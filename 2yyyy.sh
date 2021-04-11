#!/usr/bin/env bash

#for f in *.csv; do sed -i '' -E 's/([0-9]+)\/([0-9]+)\/([0-9]+)/\1-\2-\3/g' $f; done
for f in "$@"; do
    poetry run python yyy2yyyy.py "$f"
done
