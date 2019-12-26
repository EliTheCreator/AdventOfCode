import string
from math import inf


def getGraphML(graph):
    outputFile = open("graph4.graphml", "w")

    outputFile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    outputFile.write(
        '<graphml xmlns="http://graphml.graphdrawing.org/xmlns"  ')
    outputFile.write('xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  ')
    outputFile.write(
        'xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n')
    outputFile.write('  <graph id="Graph" edgedefault="directed">\n')

    for fromNode, toNodes in graph.items():
        outputFile.write(f'    <node id="{fromNode}"/>\n')

    for fromNode, toNodes in graph.items():
        for toNode in toNodes:
            outputFile.write(
                f'    <edge id="{fromNode + toNode}" source="{fromNode}" target="{toNode}"/>\n')

    outputFile.write('  </graph>\n')
    outputFile.write('</graphml>\n')

    outputFile.close()


def genGraph(baseGraph: dict, graph: dict, node: str, reachable: set):
    # print(f"gen level {str(bin(int(node[:-1]))[2:]).zfill(26)}")
    visited = set()
    toVisit = set()
    toVisit.add(node)

    while toVisit:
        nextToVisit = set()

        while toVisit:
            curNode = toVisit.pop()
            visited.add(curNode)
            curNodeLevel = curNode[:-1]
            curNodeLevelInt = int(curNode[:-1])
            curNodeName = curNode[-1]

            for childNode in baseGraph[curNodeName]:
                if childNode in string.ascii_uppercase:
                    if ((1 << (ord(childNode.lower()) - ord("a"))) & curNodeLevelInt) or (childNode.lower() not in reachable):
                        childNodeFull = curNodeLevel + childNode
                        if childNodeFull in graph:
                            graph[childNodeFull].add(curNode)
                        else:
                            graph[childNodeFull] = set([curNode])

                        graph[curNode].add(childNodeFull)

                        if childNodeFull not in visited:
                            nextToVisit.add(childNodeFull)
                elif childNode in string.ascii_lowercase:
                    if (1 << (ord(childNode) - ord("a"))) & curNodeLevelInt:
                        childNodeFull = curNodeLevel + childNode
                        if childNodeFull in graph:
                            graph[childNodeFull].add(curNode)
                        else:
                            graph[childNodeFull] = set([curNode])

                        graph[curNode].add(childNodeFull)

                        if childNodeFull not in visited:
                            nextToVisit.add(childNodeFull)
                    else:
                        childNodeFull = str(
                            (1 << (ord(childNode) - ord("a"))) | curNodeLevelInt) + childNode
                        graph[curNode].add(childNodeFull)
                        if childNodeFull not in graph:
                            graph[childNodeFull] = set()
                            genGraph(baseGraph, graph,
                                     childNodeFull, reachable)

                else:
                    childNodeFull = curNodeLevel + childNode
                    if childNodeFull in graph:
                        graph[childNodeFull].add(curNode)
                    else:
                        graph[childNodeFull] = set([curNode])

                    graph[curNode].add(childNodeFull)

                    if childNodeFull not in visited:
                        nextToVisit.add(childNodeFull)

        toVisit = nextToVisit


def main():
    file = open("input", "r")
    maze = [[x if x != "." else " " for x in line.strip()] for line in file]
    file.close()

    startNodes = ("@", "?", "!", ";")
    replacement = [[startNodes[0], "#", startNodes[1]], [
        "#", "#", "#"], [startNodes[2], "#", startNodes[3]]]
    for j in range(3):
        for i in range(3):
            maze[j + (len(maze) // 2) - 1][i +
                                           (len(maze[0]) // 2) - 1] = replacement[j][i]

    keys = {}
    doors = {}
    objectives = {}
    nodes = {}
    for j, line in enumerate(maze):
        for i, s in enumerate(line):
            if s == "#":
                continue
            elif s in string.ascii_lowercase:
                keys[s] = (j, i)
                objectives[s] = (j, i)
            elif s in string.ascii_uppercase:
                doors[s] = (j, i)
                objectives[s] = (j, i)
            elif s in startNodes:
                objectives[s] = (j, i)

            neighbours = set()
            for y, x in ((j, i-1), (j, i+1), (j-1, i), (j+1, i)):
                if maze[y][x] != "#":
                    neighbours.add((y, x))

            nodes[(j, i)] = neighbours

    baseGraph = {}
    edges = {}
    for val, rootNode in objectives.items():
        visited = set()
        toVisit = set([rootNode])
        children = {}
        dist = 0

        while toVisit:
            nextToVisit = set()
            dist += 1
            while toVisit:
                curNode = toVisit.pop()
                visited.add(curNode)
                neighbours = nodes[curNode]
                for neighbour in neighbours:
                    if neighbour not in visited:
                        y, x = neighbour
                        s = maze[y][x]
                        if s != " ":
                            visited.add(neighbour)
                            children[s] = dist
                            edges[(val, s)] = dist
                        else:
                            nextToVisit.add(neighbour)

            toVisit = nextToVisit

        baseGraph[val] = children

    quarters = {}
    for startNode in startNodes:
        reachable = set()

        visited = set()
        toVisit = set()
        toVisit.add(startNode)
        while toVisit:
            nextToVisit = set()

            while toVisit:
                curNode = toVisit.pop()
                visited.add(curNode)

                for childNode in baseGraph[curNode]:
                    if childNode not in visited:
                        if childNode in string.ascii_lowercase:
                            reachable.add(childNode)
                        toVisit.add(childNode)

            toVisit = nextToVisit
        quarters[startNode] = reachable

    graph = {}
    for startNode in startNodes:
        nodeName = "0" + startNode
        graph[nodeName] = set()
        genGraph(baseGraph, graph, nodeName, quarters[startNode])

    distances = {x: inf for x in graph.keys()}
    previous = {x: None for x in graph.keys()}
    vertexSet = set(graph.keys())
    for startNode in startNodes:
        distances["0" + startNode] = 0

    while vertexSet:
        current = min(vertexSet, key=lambda x: distances[x])

        vertexSet.remove(current)

        for neighbour in graph[current]:
            dist = baseGraph[current[-1]][neighbour[-1]]
            alt = distances[current] + dist
            if alt < distances[neighbour]:
                distances[neighbour] = alt
                previous[neighbour] = current

    minDist = 0
    for startNode in startNodes:
        level = 0
        for node in quarters[startNode]:
            level += 1 << (ord(node.lower()) - ord("a"))

        minDist += min([distances[str(level) + s]
                        for s in quarters[startNode]])

    print(minDist)


if __name__ == "__main__":
    main()
