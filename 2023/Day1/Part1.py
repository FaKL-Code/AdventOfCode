import aoc_lube
import re

LINES = aoc_lube.fetch(year=2023, day=1).splitlines()

total = 0
for line in LINES:
    a, *_, b = re.findall(r"\d", 2 * line)
    total += int(a + b)
print(total)
