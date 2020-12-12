
def main():
    file = open("input", "r")
    instructions = [(line[0], int(line[1:].strip()))
                    for line in file.readlines()]
    file.close()

    x, y = 0, 0
    direction = 1
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    for action, value in instructions:
        if action == "N":
            x += value
        elif action == "S":
            x -= value
        elif action == "E":
            y += value
        elif action == "W":
            y -= value
        elif action == "L":
            direction -= value // 90
            direction %= 4
        elif action == "R":
            direction += value // 90
            direction %= 4
        elif action == "F":
            xd, yd = directions[direction]
            x += value * xd
            y += value * yd

    print(abs(x) + abs(y))


if __name__ == "__main__":
    main()
