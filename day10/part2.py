#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 10, part 2.
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
