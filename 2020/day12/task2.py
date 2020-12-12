
def main():
    file = open("input", "r")
    instructions = [(line[0], int(line[1:].strip()))
                    for line in file.readlines()]
    file.close()

    wx, wy = 1, 10
    sx, sy = 0, 0
    for action, value in instructions:
        if action == "N":
            wx += value
        elif action == "S":
            wx -= value
        elif action == "E":
            wy += value
        elif action == "W":
            wy -= value
        elif action == "L" or action == 'R':
            if action == 'R':
                value = 360 - value
            wx_old = wx
            wy_old = wy
            direction = value // 90
            sin = (direction - 2) * ((direction - 2) % 2)
            cos = (direction - 3) * ((direction - 3) % 2)
            wx = (cos * wx_old) + (-1 * sin * wy_old)
            wy = (sin * wx_old) + (cos * wy_old)
        elif action == "F":
            sx += wx * value
            sy += wy * value

    print(abs(sx) + abs(sy))


if __name__ == "__main__":
    main()
