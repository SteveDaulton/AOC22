#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 8, part 1.

This would be a good one for numpy, but let's just do
a pain Python solution.
"""

Coords = set[tuple[int, int]]


def get_matrix(data) -> list[list[int]]:
    """Return data as matrix"""
    with open(data, encoding='ascii') as fp:
        return [[int(ch) for ch in line.strip()] for line in fp]


def scan(line: list[int], linenum: int, axis: str) -> Coords:
    """Return number visible in one row."""
    prev = -1
    rslts: Coords = set()
    lidx = len(line) - 1
    for idx, val in enumerate(line):
        if val > prev:
            if axis == 'row':
                rslts.add((idx, linenum))
            else:
                rslts.add((linenum, idx))
            prev = val
        if val == 9:  # Can't be any more.
            break
    prev = -1
    for idx, val in enumerate(reversed(line)):
        if val > prev:
            if axis == 'row':
                rslts.add((lidx - idx, linenum))
            else:
                rslts.add((linenum, lidx - idx))
            prev = val
        if val == 9:
            break
    return rslts


def scan_matrix(matrix):
    """Scan matrix horizontally and vertically.
    Return a set of coordinates of all visible trees."""
    dim: int = len(matrix)  # matrix is square.
    visible: Coords = set()
    for r_id in range(dim):
        onerow = scan(matrix[r_id], r_id, 'row')
        visible.update(onerow)

    for c_id in range(dim):
        column = [onerow[c_id] for onerow in matrix]
        visible.update(scan(column, c_id, 'col'))
    return visible


print(len(scan_matrix(get_matrix('input'))))  # 1698
