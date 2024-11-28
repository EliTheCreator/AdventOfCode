
def main():
    with open("input", "r") as file:
        data = [line.strip() for line in file.readlines()]

    sizeX = len(data[0])
    sizeY = len(data)
    horizontalLeft = [[False for _ in range(sizeX-2)] for  _ in range(sizeY-2)]
    horizontalRight = [[False for _ in range(sizeX-2)] for  _ in range(sizeY-2)]
    verticalUp = [[False for _ in range(sizeX-2)] for  _ in range(sizeY-2)]
    verticalDown = [[False for _ in range(sizeX-2)] for  _ in range(sizeY-2)]
    for y, line in enumerate(data[1:-1]):
        for x, letter in enumerate(line[1:-1]):
            match letter:
                case "<":
                    horizontalLeft[y][x] = True
                case ">":
                    horizontalRight[y][x] = True
                case "^":
                    verticalUp[y][x] = True
                case "v":
                    verticalDown[y][x] = True


    walls = set()
    for x in range(-1, sizeX-1):
        walls.add((x, -1))
        walls.add((x, sizeY-2))

    for y in range(-1, sizeY-1):
        walls.add((-1, y))
        walls.add((sizeX-2, y))


    targetX = data[-1].find(".") - 1
    targetY = sizeY - 2

    cur = set()
    next = set()
    cur.add((0, 0))
    steps = 1
    while cur:
        steps += 1
        while cur:
            curX, curY = cur.pop()
            for dx, dy in ((0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)):
                nextX = curX + dx
                nextY = curY + dy

                if (nextX, nextY) == (targetX, targetY):
                    print(steps)
                    return

                if (nextX, nextY) in walls:
                    continue

                left = (nextX + steps)%(sizeX-2)
                right = (nextX - steps)%(sizeX-2)
                up = (nextY + steps)%(sizeY-2)
                down = (nextY - steps)%(sizeY-2)

                if horizontalLeft[nextY][left] or horizontalRight[nextY][right] or verticalUp[up][nextX] or verticalDown[down][nextX]:
                    pass
                else:
                    next.add((nextX, nextY))

        cur = next
        next = set()


if __name__ == "__main__":
    main()
