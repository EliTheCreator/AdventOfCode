import re


def main():
    file = open("input", "r")
    depth = int(file.readline().strip().split()[1])
    c, r = [int(x) + 1 for x in re.findall(r"\d+", file.readline())]
    file.close()
    rc = 48271
    cc = 16807
    m = 20183
    erosionLevel = [[0 for _ in range(c)] for _ in range(r)]
    for rl in range(1, r):
        erosionLevel[rl][0] = (rc * rl + depth) % m
    for cl in range(1, c):
        erosionLevel[0][cl] = (cc * cl + depth) % m

    for rl in range(1, r):
        for cl in range(1, c):
            erosionLevel[rl][cl] = ((erosionLevel[rl - 1][cl]) *
                                    (erosionLevel[rl][cl - 1]) + depth) % m
    erosionLevel[r-1][c-1] = 0

    risk = 0
    for rl in range(r):
        for cl in range(c):
            regionType = erosionLevel[rl][cl] % 3
            risk += regionType
            # if regionType == 0:
            #     print('.', end='')
            # if regionType == 1:
            #     print('=', end='')
            # if regionType == 2:
            #     print('|', end='')
        # print("")

    print(risk)


if __name__ == "__main__":
    main()
