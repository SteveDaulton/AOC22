#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 9, part 1.
"""

from typing import Set, Tuple

Li = list[int]
Lli = list[list[int]]


def move_head(pos: list[int], direction: str) -> list[int]:
    """Update position of head"""
    if direction == 'U':
        pos[1] += 1
    elif direction == 'D':
        pos[1] -= 1
    elif direction == 'L':
        pos[0] -= 1
    else:  # Right
        pos[0] += 1
    return pos


def move_tail(head: list[int], tail: list[int]) -> list[int]:
    """Update tail position based on relative position to head."""
    xdist = head[0] - tail[0]
    ydist = head[1] - tail[1]
    if xdist > 1:
        tail[0] = head[0] - 1
        if abs(ydist) == 1:
            tail[1] = head[1]
    elif xdist < -1:
        tail[0] = head[0] + 1
        if abs(ydist) == 1:
            tail[1] = head[1]
    if ydist > 1:
        tail[1] = head[1] - 1
        if abs(xdist) == 1:
            tail[0] = head[0]
    elif ydist < -1:
        tail[1] = head[1] + 1
        if abs(xdist) == 1:
            tail[0] = head[0]
    return tail


def move(hpos: Li, tpos: Li, direction: str, steps: int) -> Lli:
    """Do move for number of steps"""
    for _ in range(steps):
        hpos = move_head(hpos, direction)
        tpos = move_tail(hpos, tpos)
        MYMAP.add(tuple(tpos))
    return [hpos, tpos]


def do_motions(data: str) -> None:
    """Do motions and print result."""
    hxy: list[int] = [0, 0]
    txy: list[int] = [0, 0]
    with open(data, encoding='ascii') as fp:
        for line in fp:
            cmd = line.split()
            hxy, txy = move(hxy, txy, cmd[0], int(cmd[1]))
    print(len(MYMAP))  # 5883


MYMAP: Set[Tuple] = set()
do_motions('input')
