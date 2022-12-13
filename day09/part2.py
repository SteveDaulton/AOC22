#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 9, part 2.
"""
from typing import Set, Tuple

Li = list[int]
Lli = list[list[int]]


def move_head(pos: Li, direction: str) -> Li:
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


def move_knot(head: Li, tail: Li) -> Li:
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


def move(rope: Lli, direction: str, steps: int) -> Lli:
    """Do move for number of steps"""
    for _ in range(steps):
        rope[0] = move_head(rope[0], direction)
        for idx, _ in enumerate(rope[1:]):
            rope[idx + 1] = move_knot(rope[idx], rope[idx + 1])
        MYMAP.add(tuple(rope[-1]))
    return rope


def do_motions(data: str) -> None:
    """Do motions and print result."""
    knots = [[0, 0] for _ in range(10)]
    with open(data, encoding='ascii') as fp:
        for line in fp:
            cmd = line.split()
            knots = move(knots, cmd[0], int(cmd[1]))
    print(len(MYMAP))  # 2367


MYMAP: Set[Tuple] = set()
do_motions('input')
