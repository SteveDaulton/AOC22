#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 8, part 2.
"""


def get_matrix(data):
    """Return data as matrix"""
    with open(data, encoding='ascii') as fp:
        return [[int(ch) for ch in line.strip()] for line in fp]


def score_row(row, nth):
    """Return score nth item in a single row or column"""
    score = 0
    rscore = 0
    for idx in range(nth+1, len(row)):
        score += 1
        if row[idx] >= row[nth]:
            break
    for idx in range(nth-1, -1, -1):
        rscore += 1
        if row[idx] >= row[nth]:
            break
    return score * rscore


def test_trees(matrix: list[list[int]]) -> None:
    """Test each tree in matrix.
    Print scenic score."""
    transposed = list(list(zip(*matrix)))
    best = 0
    for r_id, row in enumerate(matrix):
        for c_id, _ in enumerate(row):
            # Row score * column score:
            best = max(best, score_row(row, c_id) *
                       score_row(transposed[c_id], r_id))
    print(best)  # 672280


test_trees(get_matrix('input'))
