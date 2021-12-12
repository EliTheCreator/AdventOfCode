from collections import defaultdict
import re


def rec(eggnog, containers, depth):
    combinations = []
    if containers:
        combinations += rec(eggnog, containers[1:], depth)
        leftEggnog = eggnog - containers[0]
        if leftEggnog > 0:
            combinations += rec(leftEggnog, containers[1:], depth + 1)
        elif leftEggnog == 0:
            combinations += [depth]

    return combinations


def main():
    with open("input", "r") as file:
        containers = tuple(
            sorted([int(x) for x in re.findall("\d+", file.read())], reverse=True))

    counters = defaultdict(lambda: 0)
    for x in rec(150, containers, 0):
        counters[x] += 1

    print(counters[min(counters.keys())])


if __name__ == "__main__":
    main()
