#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 10, part 2.

Much trickier than part 1. The hardest part being understanding the
question :-)

The 'timer' in this case is the CRT scan which moves one px per cycle
from left to right. The CRT pixel position starts at the extreme left,
then moves one pixel (one cycle) at a time for 40 cycles, then restarts
from the zero (left) position on the next line.

The centre of the 'sprite' position is the value of the 'Register X',
and extends 1 px left and right of the Register X value.

The Register X' value is simply the accumulated values (sum of) the
'addx' commands plus one (the starting value).

A pixel is '#' when the CRT pixel position coincides with the 'sprite'
position; that is, the Register X value +/- 1.

Off-by-one issues are intended by the evil Question Master (only joking
Eric, we love you really). Use either 'pixel position' (zero indexed)
OR 'cycle count' (one indexed) and forget the other.
"""


def do_print(crt: int, sprite_pos: int) -> None:
    """Prints PLEFULPB"""
    xpos: int = crt % 40
    if xpos == 0:
        print('')  # New line
    if abs(xpos - sprite_pos) <= 1:
        print('#', end='')
    else:
        print('.', end='')


pxpos: int = 0
xreg: int = 1
add: int = 0

with open('input', encoding='ascii') as fp:
    for line in fp:
        line = line.strip()
        if line[:4] == 'noop':
            do_print(pxpos, xreg)
            pxpos += 1
        else:
            add = int(line[5:])
            do_print(pxpos, xreg)
            pxpos += 1
            do_print(pxpos, xreg)
            xreg += add
            add = 0
            pxpos += 1
