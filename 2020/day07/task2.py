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
            count, child_name = child.split(" ", maxsplit=1)
            graph[parent].add((child_name, int(count)))

    def countBags(startNode):
        localSum = sum([count + count*countBags(childNode)
                        for childNode, count in graph[startNode]])
        if localSum:
            return localSum
        else:
            return 0

    print(countBags("shiny gold"))


if __name__ == "__main__":
    main()
