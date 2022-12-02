#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 2, part 2.
Lots of ugly solutions to this problem. Here is one of them."""


VALUES: dict[str, int] = {'A': 1, 'B': 2, 'C': 3}
BEATS: dict[str, str] = {'A': 'B', 'B': 'C', 'C': 'A'}
LOSES: dict[str, str] = {'A': 'C', 'B': 'A', 'C': 'B'}


def calc_score(player1: str, player2: str) -> int:
    """Return score from one game."""
    if player2 == 'X':  # Lose
        return VALUES[LOSES[player1]]
    if player2 == 'Y':  # Draw
        return VALUES[player1] + 3
    return VALUES[BEATS[player1]] + 6


with open('input', encoding='utf-8') as fp:
    print(sum([calc_score(*line.split()) for line in fp]))  # 10349
