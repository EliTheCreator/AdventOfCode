from collections import defaultdict


class customdefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError((key,))
        self[key] = value = self.default_factory(key)
        return value


def main():
    with open("input", "r") as file:
        caveConnections = [line.strip().split("-")
                           for line in file.readlines()]

    graph = defaultdict(lambda: set())
    bigCaves = set()
    for start, end in caveConnections:
        graph[start].add(end)
        graph[end].add(start)

        for cave in (start, end):
            if cave.isupper():
                bigCaves.add(cave)

    def caveNumberatorGen():
        num = 1
        while True:
            yield num
            num <<= 1

    caveNumberator = caveNumberatorGen()
    caveNumMap = customdefaultdict(
        lambda x: 0 if x in bigCaves else caveNumberator.__next__())

    def ways(pos, visited, twice):
        if pos == "end":
            return 1

        numWays = 0

        visited |= caveNumMap[pos]
        for next in graph[pos]:
            if not (visited & caveNumMap[next]):
                numWays += ways(next, visited, twice)
            if not twice and (visited & caveNumMap[next]) and next != "start":
                numWays += ways(next, visited, True)

        return numWays

    print(ways("start", 0, False))


if __name__ == "__main__":
    main()
