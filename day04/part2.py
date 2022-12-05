#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 4, part 2."""

with open('input', encoding='utf-8') as fp:
    total: int = 0
    for line in fp:
        strt1, end1, strt2, end2 = map(int, line.replace('-', ',').split(','))
        # Easier to test if they are not overlapping.
        if not (end1 < strt2 or strt1 > end2):
            total += 1
    print(total)  # 891
