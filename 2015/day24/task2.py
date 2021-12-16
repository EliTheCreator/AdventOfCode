from functools import reduce
from itertools import combinations


def main():
    with open("input", "r") as file:
        pkts = [int(line.strip()) for line in file.readlines()]

    grpSize = sum(pkts) // 4

    candidates = set()
    for size in range(len(pkts)):
        for combination in combinations(pkts, size):
            if sum(combination) == grpSize:
                candidates.add(combination)

        if candidates:
            break

    print(min(reduce(lambda a, b: a*b, candidate) for candidate in candidates))


if __name__ == "__main__":
    main()
