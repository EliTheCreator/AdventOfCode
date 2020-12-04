import os
import re


def main():
    file = open("input", "r")
    presents = [[int(x) for x in re.findall("[0-9]+", line)]
                for line in file.readlines()]
    file.close()

    totalArea = 0
    for (l, w, h) in presents:
        sides = [l*w, l*h, w*h]
        totalArea += 2*sum(sides) + min(sides)

    print(totalArea)


if __name__ == "__main__":
    main()
