#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 16, part 1.

Wow, this one's tough. I'll probably leave this one 'till after
Christmas, but here's the input parsing.
"""

import re
from typing import Optional, Match
from dataclasses import dataclass
from itertools import permutations


@dataclass
class Valve:
    """Valve dataclass:
    Valve(name='AA',
          flow=int,
          valves=['BB', ...])
    """
    name: str
    flow: int
    valves: list[str]


def get_data(fname: str) -> list[Valve]:
    """Return parsed data from text file."""
    with open(fname, encoding='ascii') as fp:
        input_data = []
        line: str
        for line in fp:
            # Naughty Eric :-) Inconsistent lines.
            line = line.strip().replace('tunnel leads to valve',
                                        'tunnels lead to valves')
            # Keeping mypy happy
            match: Optional[Match[str]] = re.search(r'\d+', line)
            flow: int = int(match.group()) if match else 0

            valves: list = re.findall(r'[A-Z]{2}', line)
            v0: str = valves[0]
            valves = valves[1:]
            input_data.append(Valve(v0, flow, valves))
        # Probably doesn't need to be sorted, but may be useful.
        return sorted(input_data, key=lambda v: v.name)


INPUT = 'input'

VALVES = get_data(INPUT)
CLOSED = [valve for valve in VALVES if valve.flow == 0]
OPEN = [valve for valve in VALVES if valve.flow > 0]

print(len(OPEN))
perms = permutations(OPEN)
# With 1,307,674,368,000 permutations, it will not be
# possible to brute force.
#
# Each valve could be weighted according to:
# flowrate * (30 - <shortes path to get there>) == most flow possible
# from that valve.
#
# Then calculate weights to decide which valve to open next.
# If another 'working' valve has to be passed during the shortest
# path to a valve, then that will be turned on and its value added
# to the destination valve.
#
# If two valves have equal weights, then create a new branch to
# the search tree.
