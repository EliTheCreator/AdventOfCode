from math import sqrt
import re


def main():
    with open("input", "r") as file:
        data = [int(x) for x in re.findall(r"-?\d+", file.readline())]

    start = (0, 0)
    _, maxY = start
    minBoxX, maxBoxX = sorted(data[:2])
    minBoxY, maxBoxY = sorted(data[2:])

    vxLowerBound = int(sqrt(2*minBoxX + 0.25) - 0.5)
    vxUpperBound = maxBoxX + 1
    vyUpporBound = abs(minBoxY) + 1
    yLimitDown = min(0, minBoxY)
    xLimitRight = maxBoxX

    for vxStart in range(vxLowerBound, vxUpperBound):
        for vyStart in range(vyUpporBound):
            vx, vy = vxStart, vyStart
            x, y = start
            localMaxY = y

            while True:
                x += vx
                y += vy
                vx = 0 if vx == 0 else vx - (vx // abs(vx))
                vy -= 1

                if x <= xLimitRight and y >= yLimitDown:
                    localMaxY = max(y, localMaxY)
                    if x >= minBoxX and y <= maxBoxY:
                        maxY = max(localMaxY, maxY)
                        break
                else:
                    break

    print(maxY)


if __name__ == "__main__":
    main()
