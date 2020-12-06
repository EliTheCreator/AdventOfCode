import os
import re


def main():
    file = open("input", "r")
    groups = [[y for y in x.split("\n")] for x in file.read().split("\n\n")]
    file.close()

    ordA = ord('a')
    total = 0
    for group in groups:
        answers = [0 for _ in range(26)]
        for person in group:
            for c in person:
                answers[ord(c) - ordA] = 1

        total += sum(answers)

    print(total)


if __name__ == "__main__":
    main()
