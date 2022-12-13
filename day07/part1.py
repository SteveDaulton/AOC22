#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 7, part 1.

Directory names may not be unique, so we build a dict with
PurePosixPath's as keys, and directory objects as values.
"""

from pathlib import PurePosixPath as Pp


class Dir:  # pylint: disable=too-few-public-methods
    """A directory object."""
    def __init__(self, path: Pp):
        self.path = path  # fully qualified path
        self.child_paths: set[Pp] = set()
        self.size: int = 0  # sum of file sizes in this directory

    def get_size(self):
        """Return total size of directory and contents"""
        total = self.size
        for child in self.child_paths:
            total += DIRS[child].get_size()
        return total


def cd(cwd: Pp, dname: str) -> Pp:
    """Call this with every 'cd' command."""
    if dname == '/':
        return Pp('/')
    if dname == '..':
        return cwd.parent
    return cwd/dname


def calculate(data):
    """Return the answer."""
    cwd: Pp = Pp('/')
    with open(data, encoding='utf-8') as fp:
        for line in fp:
            line = line.split()  # type: ignore
            if line[0] == '$':  # command
                if line[1] == 'cd':
                    cwd = cd(cwd, line[2])
            elif line[0].isdigit():  # add a file
                DIRS[cwd].size += int(line[0])
            else:  # add a directory
                DIRS[cwd].child_paths.add(cwd/line[1])
                DIRS[cwd/line[1]] = (Dir(cwd/line[1]))
    return sum([filebytes for di in DIRS.values()
                if (filebytes := di.get_size()) <= MAXTOTAL])


DIRS = {Pp('/'): Dir(Pp('/'))}
MAXTOTAL: int = 100000

print(f'Answer = {calculate("input")}')  # 1432936
