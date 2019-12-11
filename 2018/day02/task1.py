import os
from collections import Counter


def main():
    twos = 0
    threes = 0

    file = open("input", "r")
    for line in file:
        values = list(Counter(line).values())
        if values.__contains__(2):
            twos += 1
        if values.__contains__(3):
            threes += 1

    file.close()
    print(twos * threes)


main()
