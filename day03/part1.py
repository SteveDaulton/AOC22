#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 3, part 1."""

from typing import TextIO


PRIORITY: list[str] = (
        [chr(i) for i in range(ord('a'), ord('z')+1)] +
        [chr(i) for i in range(ord('A'), ord('Z')+1)])


def get_total(data: TextIO) -> int:
    """Return sum of priorities of duplicates."""
    total: int = 0
    for line in data:
        for ch in set(line[:len(line) // 2]):  # first half (unique items)
            if ch in line[len(line) // 2:]:
                total += PRIORITY.index(ch)+1
    return total


with open('input', encoding='utf-8') as fp:
    print('Sum of the priorities of duplicates = ', get_total(fp))  # 7845


with open('input', encoding='utf-8') as fp:
    # Just for fun: As a one liner:
    print(sum([sum([PRIORITY.index(ch)+1
                    for ch in set(line[:len(line) // 2])
                    if ch in line[len(line) // 2:]])
              for line in fp]))
