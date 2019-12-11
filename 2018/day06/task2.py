import os
import re


def main():
    # file = open("E:\\Development\\AdventOfCode\\2018\\day06\\input", "r")
    file = open("input", "r")
    points = sorted([[int(x) for x in re.findall("[0-9]+", line)]
                     for line in file], key=lambda cords: cords[0])
    file.close()

    minx = points[0][0]
    maxx = points[-1][0] - minx + 1
    miny = min(points, key=lambda cords: cords[1])[1]
    maxy = max(points, key=lambda cords: cords[1])[1] - miny + 1

    for index, (px, py) in enumerate(points):
        points[index] = [px-minx, py-miny]

    distances = [[0 for _ in range(maxy)] for _ in range(maxx)]

    regionSize = 0

    for x in range(maxx):
        for y in range(maxy):

            for px, py in points:
                distances[x][y] += abs(x - px) + abs(y - py)

            if distances[x][y] < 10000:
                regionSize += 1

    print(regionSize)


main()
