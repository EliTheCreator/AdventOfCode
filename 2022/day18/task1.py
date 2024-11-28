from re import findall


def main():
    with open("input", "r") as file:
        cubes = set((tuple([int(x) for x in findall(r"\d+", line)]) for line in file.readlines()))

    neighbours = (
        (-1,  0,  0),
        ( 1,  0,  0),
        ( 0, -1,  0),
        ( 0,  1,  0),
        ( 0,  0, -1),
        ( 0,  0,  1)
    )

    totalSides = 0
    for x, y, z in cubes:
        curSides = 6
        for dx, dy, dz in neighbours:
            if (x+dx, y+dy, z+dz) in cubes:
                curSides -= 1

        totalSides += curSides

    print(totalSides)


if __name__ == "__main__":
    main()
