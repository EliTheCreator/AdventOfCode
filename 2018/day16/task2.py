import os
import re
from functools import reduce


def main():
    file = open("input", "r")
    p1, p2 = file.read().split("\n\n\n")
    file.close()
    part1 = [[[int(x) for x in re.findall(r"\d+", part)][i:i+4] for i in range(0, 12, 4)]
             for part in p1.split("\n\n")]
    part2 = [[int(x) for x in re.findall(r"\d+", line)]
             for line in p2.split("\n")][1:]

    instructions = [
        lambda r, i: r[i[1]] + r[i[2]],
        lambda r, i: r[i[1]] + i[2],
        lambda r, i: r[i[1]] * r[i[2]],
        lambda r, i: r[i[1]] * i[2],
        lambda r, i: r[i[1]] & r[i[2]],
        lambda r, i: r[i[1]] & i[2],
        lambda r, i: r[i[1]] | r[i[2]],
        lambda r, i: r[i[1]] | i[2],
        lambda r, i: r[i[1]],
        lambda r, i: i[1],
        lambda r, i: 1 if i[1] > r[i[2]] else 0,
        lambda r, i: 1 if r[i[1]] > i[2] else 0,
        lambda r, i: 1 if r[i[1]] > r[i[2]] else 0,
        lambda r, i: 1 if i[1] == r[i[2]] else 0,
        lambda r, i: 1 if r[i[1]] == i[2] else 0,
        lambda r, i: 1 if r[i[1]] == r[i[2]] else 0,
    ]
    numInstr = len(instructions)

    possibleTranslations = [[] for _ in range(numInstr)]
    for preS, instr, postS in part1:
        matching = list(filter(lambda x: x > -1, map(lambda f: f[0] if (f[1])(preS, instr) ==
                                                     postS[instr[3]] else -1, enumerate(instructions))))
        possibleTranslations[instr[0]].append(matching)

    s0 = set([x for x in range(numInstr)])
    possibleTranslations = [(i, s0.intersection(*sets))
                            for i, sets in enumerate(possibleTranslations)]

    translations = {}
    while possibleTranslations:
        m = min(possibleTranslations, key=lambda x: len(x[1]))
        possibleTranslations.remove(m)
        for i in possibleTranslations:
            i[1].difference_update(m[1])

        translations[m[0]] = m[1].pop()

    regs = [0 for _ in range(4)]
    for ins in part2:
        opcode = translations[ins[0]]
        regs[ins[3]] = (instructions[opcode])(regs, ins)

    print(regs[0])


if __name__ == "__main__":
    main()
