#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 14, part 2.

Not a nice solution, just an easy extension of part 1.
"""

import sys
from functools import reduce
from itertools import chain


def get_map(paths: list[list[list[int]]], width: int,
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
    grid.append(['.' for _ in range(width)])
    grid.append(['#' for _ in range(width)])
    return grid


def next_cell(grid: list[list[str]], x: int, y: int) -> int | None:
    """Return -1, 0, or 1 for relative x position of sand, else
    return None if no space.
    x and y are current coordinates in grid
    """
    assert x > 0, 'Overflow on left side.'
    y += 1
    if grid[y][x] == '.':
        return 0
    if grid[y][x - 1] == '.':
        return -1
    try:
        if grid[y][x + 1] == '.':
            return 1
    except IndexError:
        sys.exit('Error.\nOverflow on right side.')
    return None


def add_sand(grid: list[list[str]], offset: int) -> bool:
    """Each call will drop one unit of sand."""
    x: int = 500 - offset
    y: int = 0
    oldchar = grid[y][x]
    ok = (-1, 0, 1)
    update = False
    newx: int | None
    while (newx := next_cell(grid, x, y)) in ok:
        update = True
        grid[y][x] = oldchar
        x += newx
        y += 1
        oldchar = grid[y][x]
        grid[y][x] = 'o'
    return update


with open('input', encoding='ascii') as fp:
    coords = []
    for line in fp:
        dline = line.split('->')
        coords.append([[int(x) for x in item.strip().split(',')]
                       for item in dline])

    minx = reduce(lambda a, b: a if a[0] < b[0] else b, chain(*coords))[0]
    maxx = reduce(lambda a, b: a if a[0] > b[0] else b, chain(*coords))[0]
    maxy = reduce(lambda a, b: a if a[1] > b[1] else b, chain(*coords))[1]
    # Guess how much of 'infinite' floor is required and throw error
    # if there's not enough.
    maxx += 140
    minx -= 90

    rlen = maxx - minx + 1
    clen = maxy + 1

    for idy, pathcmd in enumerate(coords):
        for idx, xy in enumerate(pathcmd):
            coords[idy][idx][0] -= minx

    units: int = 0
    mymap = get_map(coords, rlen, clen, minx)
    while add_sand(mymap, minx):
        units += 1

print(units + 1)  # 23416
