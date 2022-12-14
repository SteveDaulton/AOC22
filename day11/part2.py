#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 11, part 2.

The first puzzle this year where performance matters.

In this case, the 'worry values' get so big after about 700 turns
that the program slows to a crawl. We get round that by reducing
very large numbers by a factor that is a multiple of all test values,
thus not affecting any of the 'divisible by' tests.
"""

from math import prod


def parse_monkey(data: list[str]) -> dict:
    """Return dict of monkey attributes."""
    m_id: int = int(data[0][-2:-1])
    worry: list[int] = [
            int(item.strip())
            for item in data[1].strip()[16:].split(',')
            ]
    op: str = data[2].strip().split()[-2]
    op_val: str = data[2].strip().split()[-1]
    test: int = int(data[3].strip().split()[-1])
    t_dest = int(data[4].strip().split()[-1])
    f_dest = int(data[5].strip().split()[-1])
    return {'id': m_id, 'worry': worry, 'op': op, 'op_val': op_val,
            'test': test, 'true': t_dest, 'false': f_dest, 'inspect': 0}


def get_monkeys(infile: str) -> list[dict]:
    """Return a list of monkey definition dicts."""
    with open(infile, encoding='ascii') as fp:
        raw: str = fp.read()
        return [parse_monkey(monkey_str.split('\n'))
                for monkey_str in raw.split('\n\n')]


monkeys: list[dict] = get_monkeys('input')
test_mult: int = 1
for monkey in monkeys:
    test_mult *= monkey['test']

for turn in range(10000):
    for monkey in monkeys:
        while len(monkey['worry']) > 0:
            monkey['inspect'] += 1
            w_val = monkey['worry'].pop()
            if monkey['op_val'] == 'old':
                opval = w_val
            else:
                opval = int(monkey['op_val'])
            if monkey['op'] == '*':
                w_val *= opval
            else:
                w_val += opval
            w_val = w_val % test_mult
            if w_val % monkey['test'] == 0:
                monkeys[monkey['true']]['worry'].append(w_val)
            else:
                monkeys[monkey['false']]['worry'].append(w_val)

inspected_totals: list[int] = sorted([monkey['inspect'] for monkey in monkeys])
# print(inspected_totals)
print(prod(inspected_totals[-2:]))  # 15693274740
