import re
from collections import defaultdict


def main():
    file = open("input", "r")
    depth = int(file.readline().strip().split()[1])
    ct, rt = [int(x) for x in re.findall(r"\d+", file.readline())]
    file.close()
    c, r = ct + 150, rt + 200
    rc, cc, m = 48271, 16807, 20183
    erosionLevel = [[0 for _ in range(c)] for _ in range(r)]
    for rl in range(1, r):
        erosionLevel[rl][0] = (rc * rl + depth) % m
    for cl in range(1, c):
        erosionLevel[0][cl] = (cc * cl + depth) % m

    for rl in range(1, r):
        for cl in range(1, c):
            erosionLevel[rl][cl] = ((erosionLevel[rl - 1][cl]) *
                                    (erosionLevel[rl][cl - 1]) + depth) % m

    regionTypes = [[0 for _ in range(c)] for _ in range(r)]
    for rl in range(r):
        for cl in range(c):
            regionTypes[rl][cl] = erosionLevel[rl][cl] % 3

    graph = defaultdict(lambda: set())
    for rl in range(r - 1):
        for cl in range(c - 1):
            lt = regionTypes[rl][cl]
            for rn, cn in ((rl, cl + 1), (rl + 1, cl)):
                nt = regionTypes[rn][cn]
                if nt


if __name__ == "__main__":
    main()
