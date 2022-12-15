#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 12, part 2.

Not much different from part 1. We just need to initialise the
starting position with all cells of height 'a' (including 'S').
"""

Coords = tuple[int, int, int]
Map = list[list[str]]


class Routefinder:
    """Creates a map from text input, and methods to
    search for paths within the map.
    """
    def __init__(self, mapdata: str) -> None:
        self.mymap: Map = [list(line) for line in mapdata.split()]
        self.map_height: int = len(self.mymap) - 1
        self.map_width: int = len(self.mymap[0]) - 1

    def altitude(self, x: int, y: int) -> int:
        """Return height as an int."""
        val = self.mymap[y][x]
        if val == 'S':
            val = 'a'
        if val == 'E':
            val = 'z'
        return ord(val)

    def neighbours(self, x0: int, y0: int) -> set[Coords]:
        """Return a set of coordinates that can be visited."""
        neighbours = set()
        for x1, y1 in ((x0, y0 - 1), (x0, y0 + 1), (x0 + 1, y0), (x0 - 1, y0)):
            if (0 <= x1 <= self.map_width and
                    0 <= y1 <= self.map_height and
                    (h1 := self.altitude(x1, y1)) <=
                    self.altitude(x0, y0) + 1):
                neighbours.add((x1, y1, h1))
        return neighbours

    def endpoint(self) -> Coords:
        """Return coordinates of end cell."""
        for col, row in enumerate(self.mymap):
            if 'E' in row:
                x: int = row.index('E')
                y: int = col
                alt: int = self.altitude(x, y)
                break
        return (x, y, alt)

    def startpoints(self) -> set[Coords]:
        """Return a list of starting points."""
        coords: set[Coords] = set()
        for idy, row in enumerate(self.mymap):
            for idx, alt in enumerate(row):
                if alt in ('S', 'a'):
                    coords.add((idx, idy, self.altitude(idx, idy)))
        return coords

    def shortest_route(self) -> int:
        """Return minimum number of steps from 's' to 'E'."""
        visited: set = set()
        end = self.endpoint()
        current = self.startpoints()
        steps = 0
        next_cells = set()
        while True:
            for cell in current:
                if cell == end:
                    return steps
                if cell not in visited:
                    for neib in self.neighbours(cell[0], cell[1]):
                        next_cells.add(neib)
                    visited.add(cell)
            current = next_cells
            next_cells = set()
            steps += 1
        raise Exception('Unexpected error')


with open('input', encoding='ascii') as fp:
    route = Routefinder(fp.read())
    print(route.shortest_route())  # 388
