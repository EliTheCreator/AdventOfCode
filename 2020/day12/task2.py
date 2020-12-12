import cmath


def main():
    file = open("input", "r")
    instructions = [(line[0], int(line[1:].strip()))
                    for line in file.readlines()]
    file.close()

    waypoint = 10 + 1j
    ship = 0j
    for action, value in instructions:
        if action == "N":
            waypoint += value * 1j
        elif action == "S":
            waypoint -= value * 1j
        elif action == "E":
            waypoint += value + 0j
        elif action == "W":
            waypoint -= value + 0j
        elif action == "L" or action == "R":
            if action == 'L':
                value = 360 - value
            direction = value // 90
            sin = (direction - 2) * ((direction - 2) % 2)
            cos = (direction - 3) * ((direction - 3) % 2)
            waypoint *= complex(cos, sin)
        elif action == "F":
            ship += value * waypoint

    print(abs(int(ship.real)) + abs(int(ship.imag)))


if __name__ == "__main__":
    main()
