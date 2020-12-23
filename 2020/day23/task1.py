import re
from collections import deque


def main():
    file = open("input", "r")
    cups = deque([int(x) for x in re.findall(r"\d", file.readline())])
    file.close()

    for _ in range(100):
        current_cup = cups[0]
        cups.rotate(-1)
        three_cups = [cups.popleft() for _ in range(3)]
        three_cups.reverse()

        next_cup = (current_cup - 2) % 9 + 1
        while next_cup in three_cups:
            next_cup = (next_cup - 2) % 9 + 1

        while cups[0] != next_cup:
            cups.rotate(-1)

        for cup in three_cups:
            cups.insert(1, cup)

        while cups[0] != current_cup:
            cups.rotate(-1)

        cups.rotate(-1)

    while cups[0] != 1:
        cups.rotate(-1)

    for i in list(cups)[1:]:
        print(i, end="")
    print("")


if __name__ == "__main__":
    main()
