from collections import defaultdict
from math import ceil
import re


def main():
    with open("input", "r") as file:
        vents = [[int(x) for x in re.findall("[0-9]+", line)]
                 for line in file.readlines()]

    grid = defaultdict(lambda: 0, [])
    overlaps = 0
    for (x1, y1, x2, y2) in vents:
        xstep = 1 if x1 <= x2 else -1
        ystep = 1 if y1 <= y2 else -1
        s = (abs(y2 - y1) + 1) / (abs(x2 - x1) + 1)
        for (r, x) in enumerate(range(x1, x2+xstep, xstep)):
            lowero = ystep * int(r * s)
            uppero = ystep * ceil((r + 1) * s)
            for y in range(y1 + lowero, y1 + uppero, ystep):
                if grid[(x, y)] == 1:
                    overlaps += 1
                grid[(x, y)] += 1

    print(overlaps)


if __name__ == "__main__":
    main()
