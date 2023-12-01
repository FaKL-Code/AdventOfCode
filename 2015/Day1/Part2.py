import aoc_lube

LINES = aoc_lube.fetch(year=2015, day=1)


def partTwo():
    floor = 0
    index = 1
    for char in LINES:
        if (char == "("):
            floor += 1
        else:
            floor -= 1
        if (floor < 0):
            break
        index += 1
    return index


aoc_lube.submit(year=2015, day=1, part=2, solution=partTwo)
