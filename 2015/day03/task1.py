import os
import re
from collections import defaultdict


def main():
    file = open("input", "r")
    directions = file.readline().strip()
    file.close()

    grid = defaultdict(lambda: 0)
    grid[(0, 0)] = 1
    x, y = (0, 0)
    houses = 1
    for direction in directions:
        if direction == '^':
            x += 1
        elif direction == 'v':
            x -= 1
        elif direction == '<':
            y -= 1
        elif direction == '>':
            y += 1

        curHouse = grid[(x, y)]
        if curHouse == 0:
            houses += 1
            grid[(x, y)] = 1
        else:
            grid[(x, y)] = curHouse + 1

    print(houses)


if __name__ == "__main__":
    main()
