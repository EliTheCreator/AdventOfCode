import os
import re
from collections import defaultdict


def main():
    file = open("input", "r")
    directions = file.readline().strip()
    file.close()

    grid = defaultdict(lambda: 0)
    grid[(0, 0)] = 2
    xSanta, ySanta = (0, 0)
    xRobo, yRobo = (0, 0)
    houses = 1
    who = 0
    for direction in directions:
        if who % 2 == 0:
            if direction == '^':
                xSanta += 1
            elif direction == 'v':
                xSanta -= 1
            elif direction == '<':
                ySanta -= 1
            elif direction == '>':
                ySanta += 1

            curHouse = grid[(xSanta, ySanta)]
            if curHouse == 0:
                houses += 1
                grid[(xSanta, ySanta)] = 1
            else:
                grid[(xSanta, ySanta)] = curHouse + 1
        else:
            if direction == '^':
                xRobo += 1
            elif direction == 'v':
                xRobo -= 1
            elif direction == '<':
                yRobo -= 1
            elif direction == '>':
                yRobo += 1

            curHouse = grid[(xRobo, yRobo)]
            if curHouse == 0:
                houses += 1
                grid[(xRobo, yRobo)] = 1
            else:
                grid[(xRobo, yRobo)] = curHouse + 1

        who += 1

    print(houses)


if __name__ == "__main__":
    main()
