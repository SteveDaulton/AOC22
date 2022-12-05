#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 5, part 2.

The same as part 1 except we don't reverse the order of
crates that are being moved.
"""

from typing import Tuple


with open('input', encoding='utf-8') as fp:
    # Get stacks of crates
    crates = []
    move_data: list[Tuple[int, ...]] = []
    for row in fp:
        layer: list[str] = []
        if '[' in row:
            for idx in range(0, len(row), 4):
                layer += (row[idx+1:idx+2].strip(),)
            crates.append(layer)
        elif len(row.split()) == 6:
            # Get move data
            _, num, _, get, _, put = row.split()
            move_data.append((int(num), int(get), int(put)))
    # Rearrage crate rows to columns. Top of column has id = 0.
    crates = [[bx for bx in col if bx] for col in zip(*crates)]
    # Finally we can move the crates around.
    for number, frm, to in move_data:
        move_stack = crates[frm - 1][:number]
        crates[to - 1] = move_stack + crates[to - 1]
        crates[frm - 1] = crates[frm - 1][number:]
    print(''.join([col[0] for col in crates]))  # BLSGJSDTS
