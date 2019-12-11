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

    areas = [0 for _ in range(len(points))]
    legal = [True for _ in range(len(points))]
    owners = [[-1 for _ in range(maxy)] for _ in range(maxx)]
    distances = [[0 for _ in range(maxy)] for _ in range(maxx)]

    for x in range(maxx):
        for y in range(maxy):
            minDist = 10000
            owner = -1
            for index, (px, py) in enumerate(points):
                dist = abs(x - px) + abs(y - py)
                if (dist < minDist):
                    minDist = dist
                    owner = index
                elif (dist == minDist):
                    owner = -2

            owners[x][y] = owner
            if owner > -1:
                areas[owner] += 1
            distances[x][y] = minDist

    for y in range(maxy):
        legal[owners[0][y]] = False
        legal[owners[maxx - 1][y]] = False

    for x in range(maxx):
        legal[owners[x][0]] = False
        legal[owners[x][maxy - 1]] = False

    results = reversed(sorted(zip(legal, areas), key=lambda x: x[1]))
    for leg, num in results:
        print(f"{leg} {num}")

    # for l in owners:
    #     print(l)

    # for radius in range(maxDist + 1):
    #     for index, point in enumerate(points):
    #         px, py = point
    #         x = px - radius
    #         y = py
    #         for i in range(2 * radius + 1):
    #             cx = x + i
    #             if cx > -1 and cx < maxx:
    #                 cy1 = y + (radius - i)
    #                 cy2 = y - (radius - i)
    #                 if -1 < cy1 and cy1 < maxy:
    #                     if radius <= distances[cx][cy1]:
    #                         prevOwner = owners[cx][cy1]
    #                         if distances[cx][cy1] > radius:
    #                             distances[cx][cy1] = radius
    #                             owners[cx][cy1] = index
    #                             areas[index] += 1
    #                         if prevOwner != -1:
    #                             areas[prevOwner] -= 1
    #                 if -1 < cy2 and cy2 < maxy:
    #                     if radius <= distances[cx][cy2]:
    #                         prevOwner = owners[cx][cy2]
    #                         if distances[cx][cy2] > radius:
    #                             distances[cx][cy2] = radius
    #                             owners[cx][cy2] = index
    #                             areas[index] += 1
    #                         if prevOwner != -1 and prevOwner != index:
    #                             areas[prevOwner] -= 1
    # for line in distances:
    #     print(line)
main()
