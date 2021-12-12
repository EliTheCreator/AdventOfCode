

def main():
    with open("input", "r") as file:
        movements = [(movement[0], int(movement[1:]))
                     for movement in file.readline().strip().split(", ")]

    x, y = 0, 0
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    currentDirection = 0

    for turn, length in movements:
        if turn == "L":
            currentDirection = (currentDirection - 1) % 4
        else:
            currentDirection = (currentDirection + 1) % 4

        dx, dy = directions[currentDirection]
        x += dx * length
        y += dy * length

    print(abs(x) + abs(y))


if __name__ == "__main__":
    main()
