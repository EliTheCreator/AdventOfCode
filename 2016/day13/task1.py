from collections import defaultdict
from itertools import count


class customdefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError((key,))
        self[key] = value = self.default_factory(key)
        return value


def isWall(c, fav):
    x, y = c
    if x < 0 or y < 0:
        return 1
    val = x*x + 3*x + 2*x*y + y + y*y + fav
    return sum((1 for x in bin(val)[2:] if x == "1")) % 2


def main():
    with open("input", "r") as file:
        fav = int(file.readline().strip())

    grid = customdefaultdict(lambda c: isWall(c, fav))

    neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = set()
    queue = [(1, 1)]
    nextQueue = []
    for step in count(0):
        while queue:
            cur = queue.pop(0)
            if cur not in visited:
                visited.add(cur)
                x, y = cur
                if x == 31 and y == 39:
                    print(step)
                    return
                for dx, dy in neighbours:
                    if not grid[(x + dx, y + dy)]:
                        nextQueue.append((x + dx, y + dy))

        queue = nextQueue
        nextQueue = []


if __name__ == "__main__":
    main()
