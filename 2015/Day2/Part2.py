import aoc_lube
from aoc_lube.utils import extract_ints, chunk

LINES = aoc_lube.fetch(year=2015, day=2)
CONTENT = tuple(map(sorted, chunk(extract_ints(LINES), n=3)))


def partTwo():
    retorno = []
    for l, w, h in CONTENT:
        retorno.append(2 * (l+w) + l * w * h)
    return sum(retorno)


aoc_lube.submit(year=2015, day=2, part=2, solution=partTwo)
