import os
import re


def main():
    file = open("input", "r")
    adapters = sorted([int(x) for x in file.readlines()])
    file.close()

    adapters.insert(0, 0)
    adapters.append(adapters[-1] + 3)

    dif1 = 0
    dif3 = 0
    for i, j in zip(adapters[:-1], adapters[1:]):
        dif = j - i
        if dif == 1:
            dif1 += 1
        elif dif == 3:
            dif3 += 1

    print(dif1 * dif3)


if __name__ == "__main__":
    main()
