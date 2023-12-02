import aoc_lube
import re

from collections import Counter
from math import prod

LINES = aoc_lube.fetch(year=2023, day=2).splitlines()


def getGames():
    for line in LINES:
        cubes = Counter()
        for n, color in re.findall(r"(\d+) (\w+)", line):
            if int(n) > cubes[color]:
                cubes[color] = int(n)
        yield cubes


def partTwo():
    GAMES = list(getGames())

    return sum(prod(game.values()) for game in GAMES)


aoc_lube.submit(year=2023, day=2, part=2, solution=partTwo)
