#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 6, part 1.
"""

from typing import Generator

TEST1 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'  # 7
TEST2 = 'bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character'  # 5
TEST3 = 'nppdvjthqldpwncqszvftbrmjlhg: first marker after character'  # 6
TEST4 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character'  # 10
TEST5 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character'  # 11


def get_data() -> str:
    """Return input string"""
    with open('input', encoding='utf-8') as fp:
        return fp.read()


data: str = get_data()
# data: str = TEST5

count: int = 4
data_zip: zip = zip(*(data[n:] for n in range(count)))
for group in data_zip:
    if len(group) == len(set(group)):
        break
    count += 1
print(count)  # 1912


# A more efficient solution:
STEP: int = 4
itt: Generator[int, None, None] = (
        idx for idx, _ in enumerate(data)
        if len(set(data[idx-STEP:idx])) == STEP)

print(next(itt))
