#!/usr/bin/env python3
# Splits base station file from opencellid.org
# Author: pulkin

import io
import gzip

open_files = {}

with open("all.csv.gz", 'rb') as f:
    f_raw = gzip.GzipFile(fileobj=f, mode='rb')
    f_txt = io.TextIOWrapper(f_raw)
    first = f_txt.readline()

    for i, l in enumerate(f_txt):
        destination = l.split(",")[1]
        if destination not in open_files:
            f_dest = open("data/{}.csv.gz".format(destination), 'wb')
            f_dest_raw = gzip.GzipFile(fileobj=f_dest, mode='wb')
            f_dest_txt = io.TextIOWrapper(f_dest_raw)
            f_dest_txt.write(first + "\n")
            open_files[destination] = (f_dest, f_dest_raw, f_dest_txt)
        open_files[destination][2].write(l + "\n")
        if i % 100000 == 0:
            print("{:.1f}M".format(i / 1e6))

for v in open_files.values():
    for _f in v[::-1]:
        _f.close()

