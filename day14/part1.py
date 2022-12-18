#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 13, part 1.

Running the test input with ANIMATION = True is quite fun, but far
too slow for the puzzle input.
"""

import os
import sys
from functools import reduce
from itertools import chain
from time import sleep


def draw_map(paths: list[list[list[int]]], width: int,
             height: int, offset: int) -> list:
    """Draw the map."""
    grid = [['.' for _ in range(width)] for _ in range(height)]
    grid[0][500 - offset] = '+'

    for path in paths:
        oldx = -1
        for x, y in path:
            if oldx == -1:
                oldx = x
                oldy = y
                continue
            for yval in range(min(oldy, y), max(oldy, y) + 1):
                for xval in range(min(oldx, x), max(oldx, x) + 1):
                    grid[yval][xval] = '#'
                oldx = x
                oldy = y
    if ANIMATE:
        os.system('clear')
        for row in grid:
            for cell in row:
                print(cell, end='')
            print()
    return grid


def next_cell(grid: list[list[str]], x: int, y: int, sand: int) -> int | None:
    """Return -1, 0, or 1 for relative x position of sand, else
    return None if no space.
    x and y are current coordinates in grid
    """
    try:
        y += 1
        if grid[y][x] == '.':
            return 0
        if grid[y][x - 1] == '.':
            return -1
        if grid[y][x + 1] == '.':
            return 1
        return None
    except IndexError:
        sys.exit(f"Units of sand = {sand}")  # 817


def add_sand(grid: list[list[str]], offset: int, sand: int) -> bool:
    """Each call will drop one unit of sand."""
    x: int = 500 - offset
    y: int = 0
    oldchar = grid[y][x]
    ok = (-1, 0, 1)
    update = False
    newx: int | None
    while (newx := next_cell(grid, x, y, sand)) in ok:
        update = True
        grid[y][x] = oldchar
        x += newx
        y += 1
        oldchar = grid[y][x]
        grid[y][x] = 'o'
        if ANIMATE:
            # Now print it.
            sleep(0.1)
            os.system('clear')
            for row in grid:
                for cell in row:
                    print(cell, end='')
                print()
    return update


ANIMATE = False  # Turn animated output on / off.

with open('input', encoding='ascii') as fp:
    coords = []
    for line in fp:
        dline = line.split('->')
        coords.append([[int(x) for x in item.strip().split(',')]
                       for item in dline])

    minx = reduce(lambda a, b: a if a[0] < b[0] else b, chain(*coords))[0]
    maxx = reduce(lambda a, b: a if a[0] > b[0] else b, chain(*coords))[0]
    # miny = 0
    maxy = reduce(lambda a, b: a if a[1] > b[1] else b, chain(*coords))[1]

    rlen = maxx - minx + 1
    clen = maxy + 1

    for idy, pathcmd in enumerate(coords):
        for idx, xy in enumerate(pathcmd):
            coords[idy][idx][0] -= minx

    units: int = 0
    mymap = draw_map(coords, rlen, clen, minx)
    while add_sand(mymap, minx, units):
        units += 1
