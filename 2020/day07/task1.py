import os
import re
from collections import defaultdict
from collections import deque


def main():
    file = open("input", "r")
    rules = [(re.findall(
        r"^(\w+.\w+).bag", x)[0], re.findall(r"(\d+.\w+.\w+).bag", x)) for x in file.readlines()]
    file.close()

    graph = defaultdict(lambda: set(), [])
    for parent, children in rules:
        for child in children:
            _, child_name = child.split(" ", maxsplit=1)
            graph[child_name].add(parent)

    visited = set()
    toVisit = deque(["shiny gold"])
    while len(toVisit):
        currentNode = toVisit.popleft()
        if currentNode not in visited:
            visited.add(currentNode)
            for childNode in graph[currentNode]:
                toVisit.append(childNode)

    print(len(visited) - 1)


if __name__ == "__main__":
    main()
