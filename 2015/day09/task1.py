from collections import defaultdict
from itertools import count, permutations


def main():
    with open("input", "r") as file:
        data = [line.strip().split() for line in file.readlines()]

    counter = count()
    ids = defaultdict(lambda: counter.__next__())
    distances = {}
    maxDist = 0
    for fromDest, _, toDest, _, distRaw in data:
        dist = int(distRaw)
        maxDist = max(maxDist, dist)
        sortedIds = tuple(sorted([ids[fromDest], ids[toDest]]))
        distances[sortedIds] = dist

    minDist = len(ids) * maxDist
    for route in permutations(ids.values()):
        totalDist = 0
        for part in zip(route, route[1:]):
            totalDist += distances[tuple(sorted(part))]

        minDist = min(minDist, totalDist)

    print(minDist)


if __name__ == "__main__":
    main()
