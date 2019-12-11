import re


def main():
    file = open("input", "r")
    tree = {}
    for line in file:
        fro, to = re.findall("[A-Z0-9]{3}", line)
        if fro in tree:
            tree[fro].add(to)
        else:
            tree[fro] = set()
            tree[fro].add(to)

        if to not in tree:
            tree[to] = set()

    dists = {}

    nodes = set()
    nodes.add('COM')
    dist = 0

    while nodes:
        nextNodes = set()
        for node in nodes:
            nextNodes |= tree[node]
            dists[node] = dist
        dist += 1
        nodes = nextNodes

    print(sum(dists.values()))


main()