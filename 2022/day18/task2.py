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

    minX, maxX = 0, 0
    minY, maxY = 0, 0
    minZ, maxZ = 0, 0
    totalSides = 0
    for x, y, z in cubes:
        minX = min(x, minX)
        maxX = max(x, maxX)
        minY = min(y, minY)
        maxY = max(y, maxY)
        minZ = min(z, minZ)
        maxZ = max(z, maxZ)
        curSides = 6
        for dx, dy, dz in neighbours:
            if (x+dx, y+dy, z+dz) in cubes:
                curSides -= 1

        totalSides += curSides

    minX -= 1
    maxX += 1
    minY -= 1
    maxY += 1
    minZ -= 1
    maxZ += 1

    cur = set([(minX, minY, minZ)])
    next = set()
    while cur:
        for x, y, z in cur:
            cubes.add((x, y, z))
            for dx, dy, dz in neighbours:
                inXBounds = minX <= x+dx <= maxX
                inYBounds = minY <= y+dy <= maxY
                inZBounds = minZ <= z+dz <= maxZ
                inBounds = inXBounds and inYBounds and inZBounds
                if (x+dx, y+dy, z+dz) not in cubes and inBounds:
                    next.add((x+dx, y+dy, z+dz))

        cur = next
        next = set()

    totalEnclosedSides = 0
    enclosedCubes = set()
    for x in range(minX+1, maxX):
        for y in range(minY+1, maxY):
            for z in range(minZ+1, maxZ):
                if (x, y, z) not in cubes:
                    curSides = 6
                    for dx, dy, dz in neighbours:
                        if (x+dx, y+dy, z+dz) in enclosedCubes:
                            curSides -= 2

                    enclosedCubes.add((x, y, z))
                    totalEnclosedSides += curSides

    print(totalSides - totalEnclosedSides)


if __name__ == "__main__":
    main()
