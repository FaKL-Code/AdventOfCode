import aoc_lube

LINES = aoc_lube.fetch(year=2015, day=2).splitlines()


def partOne():

    result = 0
    for line in LINES:
        areas = []
        sizes = line.split('x')

        l = int(sizes[0])
        w = int(sizes[1])
        h = int(sizes[2])

        areas.append(l*w)
        areas.append(w*h)
        areas.append(h*l)

        areas.sort()

        result += 2*areas[0] + 2*areas[1] + 2*areas[2] + areas[0]

    return result


aoc_lube.submit(year=2015, day=2, part=1, solution=partOne)
