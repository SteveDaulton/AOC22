#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 4, part 1."""

with open('input', encoding='utf-8') as fp:
    total: int = 0
    for line in fp:
        e1a, e1b, e2a, e2b = map(int, line.replace('-', ',').split(','))
        if (e1a <= e2a and e1b >= e2b or
                e2a <= e1a and e2b >= e1b):
            total += 1
    print(total)  # 602
