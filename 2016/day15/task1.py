from functools import reduce
import re

# Chinese Remainder Theorem
# https://en.wikipedia.org/wiki/Chinese_remainder_theorem
# https://www.youtube.com/watch?v=ru7mWZJlRQg


def get_Ni(Mi, mi):
    for Ni in range(mi):
        if (Mi * Ni) % mi == 1:
            return Ni


def main():
    with open("input", "r") as file:
        data = [[int(x) for x in re.findall(r"\d+", line)]
                for line in file.readlines()]

    chineseRemainder = [(ticks, -1 * ((pos + disc) % ticks))
                        for disc, ticks, _, pos in data]
    M = reduce(lambda x, y: x * y[0], chineseRemainder, 1)

    x = 0
    for mi, ai in chineseRemainder:
        Mi = M//mi
        x += ai * Mi * get_Ni(Mi, mi)
    x = x % M

    print(x)


if __name__ == "__main__":
    main()
