import re
from collections import deque


def main():
    file = open("input", "r")
    tasks = []
    for line in file:
        line = line.strip().split()
        if line[0] == "deal":
            if line[1] == "into":
                tasks.append((0, 0))
            else:
                tasks.append((1, int(line[-1])))
        else:
            tasks.append((2, int(line[-1])))
    file.close()

    deckSize = 119315717514047
    rounds = 101741582076661


if __name__ == "__main__":
    main()
