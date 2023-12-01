import aoc_lube

LINES = aoc_lube.fetch(year=2015, day=1)


def partOne():
    floor = 0
    for char in LINES:
        if (char == "("):
            floor += 1
        else:
            floor -= 1
    return floor


aoc_lube.submit(year=2015, day=1, part=1, solution=partOne)
