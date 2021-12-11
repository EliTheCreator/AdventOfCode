from collections import defaultdict
from itertools import count, permutations


def main():
    with open("input", "r") as file:
        data = [line.strip().split() for line in file.readlines()]

    counter = count()
    ids = defaultdict(lambda: counter.__next__())
    distances = {}
    for fromDest, _, toDest, _, distRaw in data:
        dist = int(distRaw)
        sortedIds = tuple(sorted([ids[fromDest], ids[toDest]]))
        distances[sortedIds] = dist

    maxDist = 0
    for route in permutations(ids.values()):
        totalDist = 0
        for part in zip(route, route[1:]):
            totalDist += distances[tuple(sorted(part))]

        maxDist = max(maxDist, totalDist)

    print(maxDist)


if __name__ == "__main__":
    main()
