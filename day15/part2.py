#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 15, part 2.

Had to change tack for this part for it to complete in a
reasonable time. In retrospect, this approach would have been
better for part 1.
"""

import re

XY = tuple[int, int]


def manhattan(xy1: XY, xy2: XY) -> int:
    """Return the 'Manhattan distance' between
    (x1, y1) and (x2, y2).
    """
    x1, y1, x2, y2 = xy1 + xy2
    return abs(x1 - x2) + abs(y1 - y2)


def get_frequency(x: int, y: int) -> int:
    """Return the beacon frequency."""
    return x*4000000 + y


def parse(instring: str) -> tuple[XY, XY]:
    """Return parsed input line as (sensor_xy, beacon_xy)."""
    regex = r'[-+]?[0-9]+'
    match = [int(num) for num in re.findall(regex, instring.strip())]
    sx, sy, bx, by = match
    return ((sx, sy), (bx, by))


def scanrow(rownum: int) -> bool:
    """Return list of scanned ranges covered in line 'rownum'.
    """
    scanranges: list = []
    for sensor, beacon in DATA:
        manhat: int = manhattan(sensor, beacon)
        y_dist = abs(rownum - sensor[1])
        x_width = manhat - y_dist
        if x_width > 0:
            x_range = [sensor[0] - x_width, sensor[0] + x_width]
            scanranges.append(x_range)
    rslt: list = []
    for x0, x1 in sorted(scanranges):
        try:
            if x0 <= rslt[-1][1] + 1:
                rslt[-1][1] = max(rslt[-1][1], x1)
            else:
                rslt.append([x0, x1])
        except IndexError:
            rslt.append([x0, x1])
    # Only a simple test for a gap is required as that's
    # the one and only solution.
    if len(rslt) > 1:
        print(get_frequency(rslt[0][1] + 1, rownum))  # 10826395253551
        return True
    return False


MAXVAL: int = 4000000
INPUT: str = 'input'
# MAXVAL = 20
# INPUT = 'test'

with open(INPUT, encoding='ascii') as fp:
    DATA = [parse(line) for line in fp]
    for row in range(MAXVAL):
        if scanrow(row):
            break
        # Show progress - this is slow.
        if row % 10000 == 0:
            print(row)
