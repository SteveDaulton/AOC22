#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 2, part 1.
Lots of ugly solutions to this problem. Here is one of them."""


VALUES: dict[str, int] = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
BEATS: dict[str, str] = {
        'Rock': 'Paper', 'Paper': 'Scissors', 'Scissors': 'Rock'}
CHOICES: dict[str, str] = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors',
                           'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}


def calc_score(player1: str, player2: str) -> int:
    """Return score from one game."""
    player1 = CHOICES[player1]
    player2 = CHOICES[player2]
    if player2 == BEATS[player1]:
        return VALUES[player2] + 6
    if player2 == player1:
        return VALUES[player2] + 3
    return VALUES[player2]


with open('input', encoding='utf-8') as fp:
    print(sum([calc_score(*line.split()) for line in fp]))  # 11063
