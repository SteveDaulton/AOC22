#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 3, part 2."""

from typing import TextIO
from itertools import zip_longest


PRIORITY: list[str] = (
        [chr(i) for i in range(ord('a'), ord('z')+1)] +
        [chr(i) for i in range(ord('A'), ord('Z')+1)])


def get_badge_total(data: TextIO) -> int:
    """Return the sum of the priorities of badges."""
    total: int = 0
    for line1, line2, line3 in zip_longest(*[data]*3):
        # We could use an intersection of sets, but this is quicker.
        for ch in set(line1.strip()):
            if ch in line2 and ch in line3:
                total += PRIORITY.index(ch)+1
    return total


with open('input', encoding='utf-8') as fp:
    print('Sum of the priorities of badges: ', get_badge_total(fp))  # 2790
