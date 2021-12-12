

def main():
    with open("input", "r") as file:
        movements = [(movement[0], int(movement[1:]))
                     for movement in file.readline().strip().split(", ")]

    x, y = 0, 0
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    currentDirection = 0

    visited = set([(0, 0)])
    for turn, length in movements:
        if turn == "L":
            currentDirection = (currentDirection - 1) % 4
        else:
            currentDirection = (currentDirection + 1) % 4

        dx, dy = directions[currentDirection]
        if dx:
            for _ in range(dx, dx * (length + 1), dx):
                x += dx
                if (x, y) in visited:
                    print(abs(x) + abs(y))
                    return
                else:
                    visited.add((x, y))
        if dy:
            for _ in range(dy, dy * (length + 1), dy):
                y += dy
                if (x, y) in visited:
                    print(abs(x) + abs(y))
                    return
                else:
                    visited.add((x, y))


if __name__ == "__main__":
    main()
