import math


def main():
    file = open("input", "r")
    data = set()
    for y, line in enumerate(file):
        for x, letter in enumerate(line):
            if letter == '#':
                data.add((x, y))
    file.close()

    data = list(data)
    length = len(data)
    maxObs = 0

    for i, (ox, oy) in enumerate(data):
        observable = set()

        for px, py in data[0:i]:
            dx = ox - px
            dy = oy - py

            gcd = math.gcd(dx, dy)
            observable.add((dx/gcd, dy/gcd))

        for px, py in data[i+1:length]:
            dx = ox - px
            dy = oy - py
            gcd = math.gcd(dx, dy)
            observable.add((dx/gcd, dy/gcd))

        maxObs = max(maxObs, len(observable))

    print(maxObs)


main()
