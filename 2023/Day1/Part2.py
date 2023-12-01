import aoc_lube
import re

from unicodedata import name

LINES = aoc_lube.fetch(year=2023, day=1).splitlines()

digits = {k: v for v in "123456789" for k in [v, name(v)[6:].lower()]}
total = 0
aux = "|"
for line in LINES:
    a, *_, b = re.findall(rf"(?=({aux.join(digits)}))", 2 * line)
    total += int(digits[a] + digits[b])

print(total)
