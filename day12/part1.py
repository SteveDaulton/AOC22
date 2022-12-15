#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 12, part 1.

In the map, 'a' is lowest and 'z' is highest.
'S' and 'E' are start and end points
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

    def endpoints(self) -> list[Coords]:
        """Return coordinates of start and end cells."""
        s: Coords | None = None
        e: Coords | None = None
        for col, row in enumerate(self.mymap):
            if 'S' in row:
                s = (row.index('S'), col, self.altitude(row.index('S'), col))
            if 'E' in row:
                e = (row.index('E'), col, self.altitude(row.index('E'), col))
            if s and e:
                return [s, e]
        raise Exception('Endpoints not found')

    def shortest_route(self) -> int:
        """Return minimum number of steps from 's' to 'E'."""
        visited: set = set()
        start, end = self.endpoints()
        current = self.neighbours(start[0], start[1])
        steps = 1
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
    print(route.shortest_route())  # 394
