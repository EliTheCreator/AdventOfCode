import os
import re
from functools import reduce


def main():
    file = open("input", "r")
    lines = [[y for y in x.strip()] for x in file.readlines()]
    file.close()

    width = len(lines[0])

    def toboggan_trajectory(slope):
        hstride, vstride = slope
        w = 0
        counter = 0
        for h in range(0, len(lines), vstride):
            if lines[h][w] == '#':
                counter += 1
            w = (w + hstride) % width

        return counter

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    solution = reduce(
        (lambda x, y: x*y), map(lambda x: toboggan_trajectory(x), slopes))

    print(solution)


if __name__ == "__main__":
    main()
