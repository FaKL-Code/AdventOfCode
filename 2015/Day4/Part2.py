import aoc_lube

from hashlib import md5
from itertools import count

LINES = aoc_lube.fetch(year=2015, day=4)


def partTwo():
    for i in count():
        if (md5(f"{LINES}{i}".encode()).hexdigest().startswith("000000")):
            return i


aoc_lube.submit(year=2015, day=4, part=2, solution=partTwo)
