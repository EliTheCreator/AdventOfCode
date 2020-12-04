import os
import re
from functools import reduce


def main():
    file = open("input", "r")
    presents = [[int(x) for x in re.findall("[0-9]+", line)]
                for line in file.readlines()]
    file.close()

    totalArea = 0
    for masurements in presents:
        bow = reduce(lambda x, y: x*y, masurements)
        ribbon = 2*sum(masurements) - 2*max(masurements)
        totalArea += bow + ribbon

    print(totalArea)


if __name__ == "__main__":
    main()
