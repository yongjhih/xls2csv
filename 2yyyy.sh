#!/usr/bin/env bash

for f in "$@"; do
    poetry run python yyy2yyyy.py "$f"
done
