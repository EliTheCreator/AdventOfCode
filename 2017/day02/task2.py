from itertools import permutations
import re


def main():
    with open("input", "r") as file:
        data = [[int(x) for x in re.findall(r"\d+", line)]
                for line in file.readlines()]

    result = 0
    for line in data:
        for a, b in permutations(line, 2):
            if a % b == 0:
                result += a // b

    print(result)


if __name__ == "__main__":
    main()
