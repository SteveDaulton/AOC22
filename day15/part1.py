#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 15, part 1.
"""

import re

XY = tuple[int, int]


def manhattan(xy1: XY, xy2: XY) -> int:
    """Return the 'Manhattan distance' between (x1, y1) and (x2, y2)."""
    x1, y1, x2, y2 = xy1 + xy2
    return abs(x1 - x2) + abs(y1 - y2)


def do_scan(sens: XY, beac: XY) -> None:
    """For given sensor and beacon, update SCANNED with all
    coordinates that are covered by the beacon. In other words,
    all cells that are within the Manhattan distance between
    sensor and beacon"""
    BEACONS.add(beac)
    distance = manhattan(sens, beac)
    for x_offset in range(-distance, distance + 1):
        x = sens[0] + x_offset
        dy = distance - abs(x_offset)  # length in y direction
        if SEARCHROW in range(sens[1] - dy, sens[1] + dy + 1):
            SCANNED.add((x, SEARCHROW))


SCANNED: set[XY] = set()
BEACONS: set[XY] = set()
SEARCHROW: int = 2000000
# SEARCHROW: int = 10

with open('input', encoding='ascii') as fp:
    regex = r'[-+]?\d+'
    for line in fp:
        match = [int(num) for num in re.findall(regex, line.strip())]
        do_scan((match[0], match[1]), (match[2], match[3]))

SCANNED -= BEACONS

print(len([coords for coords in list(SCANNED) if coords[1] == SEARCHROW]))
# 4793062
