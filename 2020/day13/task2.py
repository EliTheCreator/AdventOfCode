import re
from functools import reduce


def get_Ni(Mi, mi):
    for Ni in range(mi):
        if (Mi * Ni) % mi == 1:
            return Ni


def main():
    file = open("input", "r")
    _ = file.readline()
    buses = [
        int(x) if x != 'x' else 1 for x in file.readline().strip().split(',')]
    file.close()

    chineseRemainder = [(p[1], -p[0]) for p in enumerate(buses) if p[1] != 1]
    M = reduce(lambda x, y: x * y[0], chineseRemainder, 1)

    x = 0
    for mi, ai in chineseRemainder:
        Mi = M//mi
        x += ai * Mi * get_Ni(Mi, mi)
    x = x % M

    print(x)


if __name__ == "__main__":
    main()
