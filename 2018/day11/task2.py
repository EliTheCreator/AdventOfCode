import re


def main():
    file = open("input", "r")
    # file = open("day11\\input", "r")
    serial = int(file.readline())
    file.close()

    sums = [[0 for _ in range(301)] for _ in range(301)]

    for y in range(1, 301):
        for x in range(1, 301):
            p = ((((((x + 10) * y) + serial) * (x + 10)) // 100) % 10) - 5
            sums[y][x] = p + sums[y-1][x] + \
                sums[y][x-1] - sums[y-1][x-1]

    maxPower = -450000
    pos = (0, 0, 0)

    for size in range(1, 301):
        # localMax = -450000
        # localPos = (0, 0, 0)
        for y in range(size, 301):
            for x in range(size, 301):
                power = sums[y][x] - sums[y-size][x] - \
                    sums[y][x-size] + sums[y-size][x-size]

                # if localMax < power:
                #     localMax = power
                #     localPos = (x, y, size)

                if maxPower < power:
                    maxPower = power
                    pos = (x, y, size)

        # print(f"{localPos[0]},{localPos[1]},{localPos[2]}, {localMax}")

    print(f"{pos[0]-pos[2]+1},{pos[1]-pos[2]+1},{pos[2]}")


main()
