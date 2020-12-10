import os
import re


def main():
    file = open("input", "r")
    adapters = sorted([int(x) for x in file.readlines()])
    file.close()

    adapters.insert(0, 0)
    adapters.append(adapters[-1] + 3)
    adapters.extend([adapters[-1] + 4 for _ in range(3)])

    paths = [0 for _ in range(len(adapters))]
    paths[0] = 1

    for i in range(0, len(adapters)-3):
        for j in range(1, 4):
            if adapters[i+j] - adapters[i] < 4:
                paths[i+j] += paths[i]

    print(paths[-4])


if __name__ == "__main__":
    main()
