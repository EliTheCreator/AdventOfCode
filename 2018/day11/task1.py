import re


def main():
    file = open("input", "r")
    serial = int(file.readline())
    file.close()

    grid = [[((((((x + 10) * y) + serial) * (x + 10)) // 100) % 10) -
             5 for x in range(1, 301)] for y in range(1, 301)]
    maxPower = -45
    pos = (1, 1)

    for x in range(0, 297):
        for y in range(0, 297):
            curPower = sum([sum([grid[y+j][x+i] for i in range(3)])
                            for j in range(3)])
            if maxPower < curPower:
                maxPower = curPower
                pos = (x + 1, y + 1)

    print(f"{pos[0]},{pos[1]}")


main()
