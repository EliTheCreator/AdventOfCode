import os
import re


def main():
    file = open("input", "r")
    p1, _ = file.read().split("\n\n\n")
    file.close()
    part1 = [[[int(x) for x in re.findall(r"\d+", part)][i:i+4] for i in range(0, 12, 4)]
             for part in p1.split("\n\n")]

    instructions = [
        lambda s, i: s[i[1]] + s[i[2]],
        lambda s, i: s[i[1]] + i[2],
        lambda s, i: s[i[1]] * s[i[2]],
        lambda s, i: s[i[1]] * i[2],
        lambda s, i: s[i[1]] & s[i[2]],
        lambda s, i: s[i[1]] & i[2],
        lambda s, i: s[i[1]] | s[i[2]],
        lambda s, i: s[i[1]] | i[2],
        lambda s, i: s[i[1]],
        lambda s, i: i[1],
        lambda s, i: 1 if i[1] > s[i[2]] else 0,
        lambda s, i: 1 if s[i[1]] > i[2] else 0,
        lambda s, i: 1 if s[i[1]] > s[i[2]] else 0,
        lambda s, i: 1 if i[1] == s[i[2]] else 0,
        lambda s, i: 1 if s[i[1]] == i[2] else 0,
        lambda s, i: 1 if s[i[1]] == s[i[2]] else 0,
    ]

    print(sum(map(lambda x: 1 if x > 2 else 0, [len(list(filter(None, map(lambda f: f(preS, i) == postS[i[3]], instructions))))
                                                for preS, i, postS in part1])))


if __name__ == "__main__":
    main()
