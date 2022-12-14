#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 11, part 1.
"""

from math import prod


def parse_monkey(data):
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


def get_monkeys(infile):
    """Return a list of monkey definition dicts."""
    with open(infile, encoding='ascii') as fp:
        raw = fp.read()
        return [parse_monkey(monkey_str.split('\n'))
                for monkey_str in raw.split('\n\n')]


monkeys = get_monkeys('input')

for turn in range(20):
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
            w_val = w_val // 3
            if w_val % monkey['test'] == 0:
                monkeys[monkey['true']]['worry'].append(w_val)
            else:
                monkeys[monkey['false']]['worry'].append(w_val)

inspected_totals = sorted([monkey['inspect'] for monkey in monkeys])
print(prod(inspected_totals[-2:]))  # 56595
