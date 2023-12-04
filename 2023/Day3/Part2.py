import aoc_lube
import re

LINES = aoc_lube.fetch(year=2023, day=3).splitlines()
H, W = len(LINES), len(LINES[0])
MATCHES = [
    [(int(m[1]), m.span()) for m in re.finditer(r"(\d+)", line)] for line in LINES
]
COORDS = {}


def find_symbol(y, x1, x2):
    for v in [y - 1, y, y + 1]:
        for u in range(x1 - 1, x2 + 1):
            if 0 <= v < H and 0 <= u < W and LINES[v][u] not in ".0123456789":
                return v, u


def find_all_symbols():
    for y, line in enumerate(MATCHES):
        for part, (x1, x2) in line:
            if coord := find_symbol(y, x1, x2):
                COORDS.setdefault(coord, []).append(part)


def partTwo():
    find_all_symbols()
    return sum(a * b[0] for a, *b in COORDS.values() if b)


aoc_lube.submit(year=2023, day=3, part=2, solution=partTwo)
