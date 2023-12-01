import aoc_lube

from itertools import accumulate

LINES = aoc_lube.fetch(year=2015, day=3)

MOVES = {
    "^": 1j,
    "v": -1j,
    "<": -1,
    ">": 1,
}

CONTENT = [MOVES[m] for m in LINES]


def calculation(*movimentos):
    unique = {0}
    for move in movimentos:
        unique.update(accumulate(move))
    return len(unique)


def partOne():
    return calculation(CONTENT)


aoc_lube.submit(year=2015, day=3, part=1, solution=partOne)
