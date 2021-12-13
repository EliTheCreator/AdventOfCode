

def main():
    with open("input", "r") as file:
        coordsAndInstrs = file.read().split("\n\n")

    coords = set(((lambda x: (int(x[0]), int(x[1])))(line.strip().split(","))
                  for line in coordsAndInstrs[0].split("\n")))

    instructions = [(lambda x: (x[0][-1], int(x[1])))(line.strip().split("="))
                    for line in coordsAndInstrs[1].split("\n")]

    for axis, axisPos in instructions:
        match axis:
            case "x":
                for x, y in list(coords):
                    if x > axisPos:
                        newx = axisPos - (x - axisPos)
                        coords.remove((x, y))
                        coords.add((newx, y))
            case "y":
                for x, y in list(coords):
                    if y > axisPos:
                        newy = axisPos - (y - axisPos)
                        coords.remove((x, y))
                        coords.add((x, newy))
            case _:
                pass

    maxx, _ = max(coords, key=lambda x: x[0])
    _, maxy = max(coords, key=lambda x: x[1])

    for y in range(maxy + 1):
        for x in range(maxx + 1):
            if (x, y) in coords:
                print("#", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    main()
