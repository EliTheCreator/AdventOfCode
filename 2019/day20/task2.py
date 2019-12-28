import string
from math import inf as INFINITY


def getGraphML(graph):
    outputFile = open("graph2.graphml", "w")

    outputFile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    outputFile.write(
        '<graphml xmlns="http://graphml.graphdrawing.org/xmlns"  ')
    outputFile.write('xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  ')
    outputFile.write(
        'xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n')
    outputFile.write('  <graph id="graph" edgedefault="directed">\n')

    for fromNode in graph.keys():
        outputFile.write(f'    <node id="{fromNode}"/>\n')

    for fromNode, toNodes in graph.items():
        for toNode in toNodes:
            outputFile.write(
                f'    <edge id="{fromNode + toNode}" source="{fromNode}" target="{toNode}"/>\n')

    outputFile.write('  </graph>\n')
    outputFile.write('</graphml>\n')

    outputFile.close()


def genLevel(baseGraph: dict, graph: dict, level: int, distances: dict, previous: dict, vertexSet: set):
    for node in baseGraph.keys():
        if node not in ("AA", "ZZ"):
            curNode = str(level) + node
            if curNode not in graph:
                distances[curNode] = INFINITY
                previous[curNode] = None
                vertexSet.add(curNode)

            neighbours = set()
            for childNode in baseGraph[node].keys():
                if childNode not in ("AA", "ZZ"):
                    if childNode[:-1] == node[:-1]:
                        if node[-1] == "O":
                            neighbours.add(str(level - 1) + childNode)
                        else:
                            neighbours.add(str(level + 1) + childNode)

                    else:
                        neighbours.add(str(level) + childNode)

            for node in neighbours:
                if node not in graph:
                    graph[node] = set()
                    distances[node] = INFINITY
                    previous[node] = None
                    vertexSet.add(node)
            graph[curNode] = neighbours


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

    outerPortals = {}
    for x in range(maxX + 1):
        if data[2][x] == ".":
            startName = "".join([data[0][x], data[1][x]])
            if startName not in ("AA", "ZZ"):
                startName += "O"
            outerPortals[(2, x)] = startName

        if data[maxY-2][x] == ".":
            startName = "".join([data[maxY - 1][x], data[maxY][x]])
            if startName not in ("AA", "ZZ"):
                startName += "O"
            outerPortals[(maxY - 2, x)] = startName

    for y in range(maxY + 1):
        if data[y][2] == ".":
            startName = "".join([data[y][0], data[y][1]])
            if startName not in ("AA", "ZZ"):
                startName += "O"
            outerPortals[(y, 2)] = startName

        if data[y][maxX-2] == ".":
            startName = "".join([data[y][maxX - 1], data[y][maxX]])
            if startName not in ("AA", "ZZ"):
                startName += "O"
            outerPortals[(y, maxX - 2)] = startName

    innerPortals = {}
    for x in range(leftDist, rightDist + 1):
        if data[topDist][x] == ".":
            startName = "".join([data[topDist+1][x], data[topDist+2][x]])
            if startName not in ("AA", "ZZ"):
                startName += "I"
            innerPortals[(topDist, x)] = startName

        if data[botDist][x] == ".":
            startName = "".join([data[botDist-2][x], data[botDist-1][x]])
            if startName not in ("AA", "ZZ"):
                startName += "I"
            innerPortals[(botDist, x)] = startName

    for y in range(topDist, botDist + 1):
        if data[y][leftDist] == ".":
            startName = "".join([data[y][leftDist+1], data[y][leftDist+2]])
            if startName not in ("AA", "ZZ"):
                startName += "I"
            innerPortals[(y, leftDist)] = startName

        if data[y][rightDist] == ".":
            startName = "".join([data[y][rightDist-2], data[y][rightDist-1]])
            if startName not in ("AA", "ZZ"):
                startName += "I"
            innerPortals[(y, rightDist)] = startName

    portals = {}
    portals.update(innerPortals)
    portals.update(outerPortals)

    baseGraph = {}
    for (y, x), startName in portals.items():
        visited = set()
        toVisit = set()
        toVisit.add((y, x))
        dist = 0
        ends = {}

        while toVisit:
            nextToVisit = set()

            while toVisit:
                node = toVisit.pop()
                visited.add(node)
                y, x = node

                for childNode in ((y, x-1), (y, x+1), (y-1, x), (y+1, x)):
                    cy, cx = childNode
                    if data[cy][cx] == "#":
                        continue
                    elif data[cy][cx] in string.ascii_uppercase:
                        endName = portals[(y, x)]

                        if startName != endName:
                            ends[endName] = dist

                            if endName in baseGraph:
                                baseGraph[endName][startName] = dist
                            else:
                                baseGraph[endName] = {startName: dist}
                    elif childNode not in visited:
                        nextToVisit.add(childNode)

            dist += 1
            toVisit = nextToVisit

        if startName in baseGraph:
            baseGraph[startName].update(ends)
        else:
            baseGraph[startName] = ends

    for node in outerPortals.values():
        if node not in ("AA", "ZZ"):
            baseGraph[node][node[:-1] + "I"] = 1

    for node in innerPortals.values():
        if node not in ("AA", "ZZ"):
            baseGraph[node][node[:-1] + "O"] = 1

    maxLevel = 0
    graph = {}
    for node in baseGraph.keys():
        if node[-1] != "O":
            neighbours = set()
            for childNode in baseGraph[node].keys():
                if childNode[-1] != "O":
                    neighbours.add("0" + childNode)
                elif node[:-1] == childNode[:-1]:
                    neighbours.add("1" + childNode)

            graph["0" + node] = neighbours

    # for fro, tos in sorted(graph.items(), key=lambda x: x[0]):
    #     print(f"{fro}: {[x for x in sorted(tos, key=lambda x: x[0])]}")

    distances = {x: INFINITY for x in graph.keys()}
    previous = {x: None for x in graph.keys()}
    vertexSet = set(graph.keys())
    distances["0AA"] = 0

    while vertexSet:
        curNode = min(vertexSet, key=lambda x: distances[x])
        curNodeName = ""

        if len(curNode) == 3:
            curNodeName = curNode[-2:]
        else:
            curNodeName = curNode[-3:]

        vertexSet.remove(curNode)

        for nextNode in graph[curNode]:
            nextNodeLevel = 0
            nextNodeName = ""
            if len(nextNode) == 3:
                nextNodeName = nextNode[-2:]
            else:
                nextNodeLevel = int(nextNode[:-3])
                nextNodeName = nextNode[-3:]

            if nextNodeLevel > maxLevel and nextNodeLevel < 30:
                genLevel(baseGraph, graph, nextNodeLevel,
                         distances, previous, vertexSet)
                maxLevel += 1

            alt = distances[curNode] + baseGraph[curNodeName][nextNodeName]
            if alt < distances[nextNode]:
                distances[nextNode] = alt
                previous[nextNode] = curNode

    print(distances["0ZZ"])

    # for fro, tos in sorted(baseGraph.items(), key=lambda x: x[0]):
    #     print(f"{fro}: {[x for x in sorted(tos.items(), key=lambda x: x[1])]}")


if __name__ == "__main__":
    main()
