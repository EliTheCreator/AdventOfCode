
def main():
    with open("input", "r") as file:
        shapes = [[[int(x) for x in pair.split(",")] for pair in line.strip().split(" -> ")]
                for line in file.readlines()]

    minX = min([min(shape, key=lambda pair: pair[0])[0] for shape in shapes]) - 2
    maxX = max([max(shape, key=lambda pair: pair[0])[0] for shape in shapes]) + 3
    minY = min([min(shape, key=lambda pair: pair[1])[1] for shape in shapes]) - 10
    maxY = max([max(shape, key=lambda pair: pair[1])[1] for shape in shapes]) + 3

    cave = [["." for _ in range(maxY-minY)] for _ in range(maxX-minX)]
    for shape in shapes:
        for (startX, startY), (endX, endY) in zip(shape[:-1], shape[1:]):
            if startX == endX:
                curX = startX-minX
                startY = startY-minY
                endY = endY-minY
                for curY in range(min(startY, endY), max(startY, endY)+1):
                    cave[curX][curY] = "#"
            if startY == endY:
                curY = startY-minY
                startX = startX-minX
                endX = endX-minX
                for curX in range(min(startX, endX), max(startX, endX)+1):
                    cave[curX][curY] = "#"

    curX = 500-minX
    curY = 0
    sandCount = 0
    while curY < maxY-minY-1:
        left = cave[curX-1][curY+1]
        mid = cave[curX][curY+1]
        right = cave[curX+1][curY+1]

        match (left, mid, right):
            case _, ".", _:
                curY += 1
            case ".", "#", _:
                curX -= 1
                curY += 1
            case "#", "#", ".":
                curX += 1
                curY += 1
            case "#", "#", "#":
                cave[curX][curY] = "#"
                curX = 500-minX
                curY = 0
                sandCount += 1
            case _:
                pass

    print(sandCount)


if __name__ == "__main__":
    main()
