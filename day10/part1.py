#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 10, part 1.
"""

xval: int = 1
cycle_num: int = 0
total: int = 0
checkpoint: int = 20

with open('input', encoding='ascii') as fp:
    val: str | None
    for line in fp:
        try:
            _, val = line.split()
        except ValueError:
            val = None
        if val:
            cycle_num += 2
        else:
            cycle_num += 1
        if cycle_num >= checkpoint:
            total += checkpoint * xval
            checkpoint += 40
        if val:
            xval += int(val)
    print(total)  # 16480
