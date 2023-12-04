import aoc_lube
import numpy as np
import re

from scipy.ndimage import convolve

LINES = aoc_lube.fetch(year=2023, day=3).splitlines()
H, W = len(GRID), len(GRID[0])
MATCHES = [
    [(int(m[1]), m.span()) for m in re.finditer(r"(\d+)", line)] for line in GRID
]
COORDS = {}


def convolution():
    operators = np.array([[int(char != "." and not char.isdigit())
                         for char in line] for line in GRID])
    spread = convolve(operators, np.ones((3, 3))).astype(bool)
    coded = np.zeros((H, W), int)
    numbers = []
    for y, line in enumerate(GRID):
        for m in re.finditer(r"(\d+)", line):
            numbers.append(int(m[0]))
            coded[y, m.start(): m.end()] = len(numbers)
    translate = np.array(numbers)
    return sum(translate[np.unique(coded[spread & (coded != 0)] - 1)])


def partOne():
    return convolution()


aoc_lube.submit(year=2023, day=3, part=1, solution=partOne)
