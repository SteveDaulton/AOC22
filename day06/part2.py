#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 6, part 2.
"""

TEST1 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'  # 19
TEST2 = 'bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character'  # 23
TEST3 = 'nppdvjthqldpwncqszvftbrmjlhg: first marker after character'  # 23
TEST4 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character'  # 29
TEST5 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character'  # 26


def get_data() -> str:
    """Return input string"""
    with open('input', encoding='utf-8') as fp:
        return fp.read()


# data: str = TEST5
data: str = get_data()

count: int = 14
data_zip: zip = zip(*(data[n:] for n in range(count)))
for group in data_zip:
    if len(group) == len(set(group)):
        break
    count += 1
print(count)  # 2122

# As a one-liner:
print(next(idx for idx, _ in enumerate(data)
           if len(set(data[idx-14:idx])) == 14))
