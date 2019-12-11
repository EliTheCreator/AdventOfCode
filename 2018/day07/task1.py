import re


def main():
    file = open("input", "r")
    edges = [[x.strip() for x in re.findall(" [A-Z] ", line)] for line in file]
    file.close()

    tree = {}
    isRoot = set([x[0] for x in edges] + [x[1] for x in edges])

    tree = {}
    inDegree = {}
    for vertex in isRoot:
        tree[vertex] = set()
        inDegree[vertex] = 0

    for fro, to in edges:
        if to in isRoot:
            isRoot.remove(to)
        tree[fro].add(to)
        inDegree[to] += 1

    avSet = isRoot
    av = sorted(avSet)
    solution = []

    while av:
        vertex = av.pop(0)
        avSet.remove(vertex)
        solution.append(vertex)

        for child in tree[vertex]:
            if inDegree[child] == 1:
                avSet.add(child)
            else:
                inDegree[child] -= 1

        av = sorted(avSet)

    print("".join(solution))


main()
