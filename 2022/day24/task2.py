
def main():
    with open("input", "r") as file:
        data = [line.strip() for line in file.readlines()]

    sizeX = len(data[0])
    sizeY = len(data)

    startY = 0
    startX = data[startY].find(".")
    targetY = sizeY-1
    targetX = data[targetY].find(".")

    walls = set()
    for x in range(-1, sizeX+1):
        walls.add((x, -1))
        walls.add((x, 0))
        walls.add((x, sizeY-1))
        walls.add((x, sizeY))
    for y in range(-1, sizeY+1):
        walls.add((-1, y))
        walls.add((0, y))
        walls.add((sizeX-1, y))
        walls.add((sizeX, y))
    walls.remove((startX, startY))
    walls.remove((targetX, targetY))

    horizontalLeft = [[False for _ in range(sizeX)] for  _ in range(sizeY)]
    horizontalRight = [[False for _ in range(sizeX)] for  _ in range(sizeY)]
    verticalUp = [[False for _ in range(sizeX)] for  _ in range(sizeY)]
    verticalDown = [[False for _ in range(sizeX)] for  _ in range(sizeY)]
    for y, line in enumerate(data):
        for x, letter in enumerate(line):
            match letter:
                case "<":
                    horizontalLeft[y][x] = True
                case ">":
                    horizontalRight[y][x] = True
                case "^":
                    verticalUp[y][x] = True
                case "v":
                    verticalDown[y][x] = True

    def find_path(steps, startX, startY, targetX, targetY):
        cur = set()
        next = set()
        cur.add((startX, startY))
        while cur:
            steps += 1
            while cur:
                curX, curY = cur.pop()
                for dx, dy in ((0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)):
                    nextX = curX + dx
                    nextY = curY + dy

                    if (nextX, nextY) == (startX, startY):
                        next.add((nextX, nextY))
                        continue

                    if (nextX, nextY) == (targetX, targetY):
                        return steps

                    if (nextX, nextY) in walls:
                        continue

                    left = (nextX-1 + steps)%(sizeX-2) + 1
                    right = (nextX-1 - steps)%(sizeX-2) + 1
                    up = (nextY-1 + steps)%(sizeY-2) + 1
                    down = (nextY-1 - steps)%(sizeY-2) + 1

                    if horizontalLeft[nextY][left] or horizontalRight[nextY][right] or verticalUp[up][nextX] or verticalDown[down][nextX]:
                        pass
                    else:
                        next.add((nextX, nextY))

            cur = next
            next = set()

    steps = 0
    for locations in ((startX, startY, targetX, targetY), (targetX, targetY, startX, startY), (startX, startY, targetX, targetY)):
        steps = find_path(steps, *locations)
    print(steps)


if __name__ == "__main__":
    main()
