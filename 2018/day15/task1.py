import re


class Goblin:
    pos: tuple


def main():
    file = open("input", "r")
    data = [[s for s in row.strip()] for row in file]
    file.close()
    elves = set()
    goblins = set()
    units = set()

    for line in data:
        print(line)


if __name__ == "__main__":
    main()
