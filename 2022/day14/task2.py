from collections import defaultdict


class customdefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError((key,))
        self[key] = value = self.default_factory(key)
        return value


def main():
    with open("input", "r") as file:
        shapes = [[[int(x) for x in pair.split(",")] for pair in line.strip().split(" -> ")]
                for line in file.readlines()]

    floorY = max([max(shape, key=lambda pair: pair[1])[1] for shape in shapes]) + 2
    cave = customdefaultdict(lambda cord: True if cord[1] >= floorY else False)
    for shape in shapes:
        for (startX, startY), (endX, endY) in zip(shape[:-1], shape[1:]):
            if startX == endX:
                for curY in range(min(startY, endY), max(startY, endY)+1):
                    cave[(startX, curY)] = True
            if startY == endY:
                for curX in range(min(startX, endX), max(startX, endX)+1):
                    cave[(curX, startY)] = True

    curX = 500
    curY = 0
    sandCount = 0
    while not cave[(500, 0)]:
        left = cave[(curX-1, curY+1)]
        mid = cave[(curX, curY+1)]
        right = cave[(curX+1, curY+1)]

        match (left, mid, right):
            case _, False, _:
                curY += 1
            case False, True, _:
                curX -= 1
                curY += 1
            case True, True, False:
                curX += 1
                curY += 1
            case True, True, True:
                cave[(curX, curY)] = True
                curX = 500
                curY = 0
                sandCount += 1
            case _:
                pass

    print(sandCount)


if __name__ == "__main__":
    main()
