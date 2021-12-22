import re


def main():
    with open("input", "r") as file:
        cubes = [(line.split(" ")[0], [int(x) for x in re.findall(r"-?\d+", line)])
                 for line in file.readlines()]

    ons = set()
    for mode, (lx, hx, ly, hy, lz, hz) in cubes[:20]:
        curCube = set()
        for x in range(lx, hx + 1):
            for y in range(ly, hy + 1):
                for z in range(lz, hz + 1):
                    curCube.add((x, y, z))

        if mode == "on":
            ons |= curCube
        else:
            ons -= curCube

    print(len(ons))


if __name__ == "__main__":
    main()
