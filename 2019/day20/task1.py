import string
from math import inf as INFINITY


def main():
    file = open("input", "r")
    data = [[x for x in line.strip("\n")] for line in file]
    file.close()

    maxY = len(data) - 1
    maxX = len(data[0]) - 1

    topDist, botDist, leftDist, rightDist = 2, maxY-2, 2, maxX-2
    midX = maxX // 2
    midY = maxY // 2
    while data[midY][leftDist+1] in (".", "#"):
        leftDist += 1
    while data[midY][rightDist-1] in (".", "#"):
        rightDist -= 1
    while data[topDist+1][midX] in (".", "#"):
        topDist += 1
    while data[botDist-1][midX] in (".", "#"):
        botDist -= 1

    outerPortals = set()
    for x in range(maxX + 1):
        if data[2][x] == ".":
            startName = "".join([data[0][x], data[1][x]])
            outerPortals.add((startName, (2, x)))

        if data[maxY-2][x] == ".":
            startName = "".join([data[maxY - 1][x], data[maxY][x]])
            outerPortals.add((startName, (maxY - 2, x)))

    for y in range(maxY + 1):
        if data[y][2] == ".":
            startName = "".join([data[y][0], data[y][1]])
            outerPortals.add((startName, (y, 2)))

        if data[y][maxX-2] == ".":
            startName = "".join([data[y][maxX - 1], data[y][maxX]])
            outerPortals.add((startName, (y, maxX - 2)))

    innerPortals = set()
    for x in range(leftDist, rightDist + 1):
        if data[topDist][x] == ".":
            startName = "".join([data[topDist+1][x], data[topDist+2][x]])
            innerPortals.add((startName, (topDist, x)))

        if data[botDist][x] == ".":
            startName = "".join([data[botDist-2][x], data[botDist-1][x]])
            innerPortals.add((startName, (botDist, x)))

    for y in range(topDist, botDist + 1):
        if data[y][leftDist] == ".":
            startName = "".join([data[y][leftDist+1], data[y][leftDist+2]])
            innerPortals.add((startName, (y, leftDist)))

        if data[y][rightDist] == ".":
            startName = "".join([data[y][rightDist-2], data[y][rightDist-1]])
            innerPortals.add((startName, (y, rightDist)))

    portals = innerPortals | outerPortals

    graph = {}
    for portal in portals:
        startName, (y, x) = portal
        visited = set()
        toVisit = set()
        toVisit.add((y, x))
        dist = 0
        ends = set()

        while toVisit:
            nextToVisit = set()

            while toVisit:
                node = toVisit.pop()
                visited.add(node)
                y, x = node

                for direction, childNode in enumerate(((y, x-1), (y, x+1), (y-1, x), (y+1, x))):
                    cy, cx = childNode
                    if data[cy][cx] == "#":
                        continue
                    elif data[cy][cx] in string.ascii_uppercase:
                        endName = ""
                        if direction == 0:
                            endName = "".join([data[cy][cx-1], data[cy][cx]])
                        elif direction == 1:
                            endName = "".join([data[cy][cx], data[cy][cx+1]])
                        elif direction == 2:
                            endName = "".join([data[cy-1][cx], data[cy][cx]])
                        elif direction == 3:
                            endName = "".join([data[cy][cx], data[cy+1][cx]])

                        if startName != endName:
                            ends.add((endName, dist))

                            if endName in graph:
                                graph[endName].add((startName, dist))
                            else:
                                graph[endName] = set([(startName, dist)])
                    elif childNode not in visited:
                        nextToVisit.add(childNode)

            dist += 1
            toVisit = nextToVisit

        if startName in graph:
            graph[startName] |= ends
        else:
            graph[startName] = ends

    distances = {x: INFINITY for x in graph.keys()}
    previous = {x: None for x in graph.keys()}
    vertexSet = set(graph.keys())
    distances["AA"] = 0

    while vertexSet:
        current = min(vertexSet, key=lambda x: distances[x])

        vertexSet.remove(current)

        for neighbour, dist in graph[current]:
            alt = distances[current] + dist
            if alt < distances[neighbour]:
                distances[neighbour] = alt
                previous[neighbour] = current

    path = ["ZZ"]
    while previous[path[-1]] != None:
        path.append(previous[path[-1]])

    # for fro, tos in sorted(graph.items(), key=lambda x: x[0]):
    #     print(f"{fro}: {[x for x in sorted(tos, key=lambda x: x[0])]}")
    # print(list(reversed(path)))
    print(distances["ZZ"] + len(path) - 2)


if __name__ == "__main__":
    main()


def getGraphML(graph):
    outputFile = open("graph.graphml", "w")

    outputFile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    outputFile.write(
        '<graphml xmlns="http://graphml.graphdrawing.org/xmlns"  ')
    outputFile.write('xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  ')
    outputFile.write(
        'xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n')
    outputFile.write('  <graph id="G" edgedefault="undirected">\n')

    for fromNode in graph.keys():
        outputFile.write(f'    <node id="{fromNode}"/>\n')

    for fromNode, toNodes in graph.items():
        for toNode, distance in toNodes:
            outputFile.write(
                f'    <edge id="{fromNode + toNode}" source="{fromNode}" target="{toNode}" weight="{str(distance)}"/>\n')

    outputFile.write('  </graph>\n')
    outputFile.write('</graphml>\n')

    outputFile.close()
