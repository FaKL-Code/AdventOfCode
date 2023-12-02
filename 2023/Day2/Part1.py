import aoc_lube
import re

from collections import Counter

LINES = aoc_lube.fetch(year=2023, day=2).splitlines()


def getGames():
    for line in LINES:
        cubes = Counter()
        for n, color in re.findall(r"(\d+) (\w+)", line):
            if int(n) > cubes[color]:
                cubes[color] = int(n)
        yield cubes


def partOne():
    GAMES = list(getGames())

    maximum = Counter({"red": 12, "green": 13, "blue": 14})
    return sum(i for i, game in enumerate(GAMES, start=1) if game <= maximum)


aoc_lube.submit(year=2023, day=2, part=1, solution=partOne)
