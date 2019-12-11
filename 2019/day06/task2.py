import re


def main():
    file = open("input", "r")
    tree = {}
    for line in file:
        fro, to = re.findall("[A-Z0-9]+", line)
        if fro not in tree:
            tree[fro] = set()
        tree[fro].add(to)

        if to not in tree:
            tree[to] = set()
        tree[to].add(fro)

    visited = set()
    nodes = set()
    nodes.add('YOU')
    dist = -1
    found = False

    while not found:
        dist += 1
        nextNodes = set()
        for node in nodes:
            visited.add(node)
            nextNodes |= tree[node]
            if node == 'SAN':
                found = True
                break
        nodes = nextNodes ^ (nextNodes & visited)

    print(dist-2)


main()