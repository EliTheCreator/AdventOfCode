import re


def main():
    with open("input", "r") as file:
        cuboidsRaw = [(line.split(" ")[0], tuple([int(x) for x in re.findall(r"-?\d+", line)]))
                      for line in file.readlines()]

    def intersectionCuboid(c1, c2):
        lx1, hx1, ly1, hy1, lz1, hz1 = c1
        lx2, hx2, ly2, hy2, lz2, hz2 = c2

        for end, start in zip((hx2, hy2, hz2), (lx1, ly1, lz1)):
            if end < start:
                return None

        for end, start in zip((hx1, hy1, hz1), (lx2, ly2, lz2)):
            if end < start:
                return None

        lx3 = lx1 if lx1 > lx2 else lx2
        hx3 = hx1 if hx1 < hx2 else hx2
        ly3 = ly1 if ly1 > ly2 else ly2
        hy3 = hy1 if hy1 < hy2 else hy2
        lz3 = lz1 if lz1 > lz2 else lz2
        hz3 = hz1 if hz1 < hz2 else hz2
        return (lx3, hx3, ly3, hy3, lz3, hz3)

    def intersectCuboids(c1, c2):
        c3 = intersectionCuboid(c1, c2)
        if c3 is not None:
            lx1, hx1, ly1, hy1, lz1, hz1 = c1
            lx3, hx3, ly3, hy3, lz3, hz3 = c3
            newCubes = []
            if lz1 < lz3:
                newCubes.append((lx1, hx1, ly1, hy1, lz1, lz3 - 1))
            if hz1 > hz3:
                newCubes.append((lx1, hx1, ly1, hy1, hz3 + 1, hz1))
            if ly1 < ly3:
                newCubes.append((lx1, hx1, ly1, ly3 - 1, lz3, hz3))
            if hy1 > hy3:
                newCubes.append((lx1, hx1, hy3 + 1, hy1, lz3, hz3))
            if lx1 < lx3:
                newCubes.append((lx1, lx3 - 1, ly3, hy3, lz3, hz3))
            if hx1 > hx3:
                newCubes.append((hx3 + 1, hx1, ly3, hy3, lz3, hz3))

            return newCubes
        else:
            return [c1]

    cuboids = []
    for mode, newCuboid in cuboidsRaw:
        newCuboids = []
        for oldCuboid in cuboids:
            newCuboids += intersectCuboids(oldCuboid, newCuboid)
        if mode == "on":
            newCuboids.append(newCuboid)
        cuboids = newCuboids

    totalCubesOn = 0
    for lx, hx, ly, hy, lz, hz in cuboids:
        totalCubesOn += (hx - lx + 1) * (hy - ly + 1) * (hz - lz + 1)

    print(totalCubesOn)


if __name__ == "__main__":
    main()
