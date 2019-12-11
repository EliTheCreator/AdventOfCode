import math


def main():
    file = open("input", "r")
    data = set()
    for y, line in enumerate(file):
        for x, letter in enumerate(line):
            if letter == '#':
                data.add((x, y))
    file.close()

    coords = (26, 36)

    data.remove(coords)
    observable = {}

    ox, oy = coords
    for px, py in data:
        dx = px - ox
        dy = py - oy
        dist = math.sqrt(dx**2 + dy**2)

        gcd = math.gcd(dx, dy)
        gdx = dx // gcd
        gdy = dy // gcd
        gdist = math.sqrt(gdx**2 + gdy**2)
        key = gdy / gdist
        if dx < 0:
            key = 2 + (-1 * key)

        if key in observable:
            observable[key].append((dist, px, py))
        else:
            observable[key] = [(dist, px, py)]

    for key in observable.keys():
        observable[key] = sorted(observable[key], key=lambda x: x[0])

    counter = 0
    i = 0
    last = (0, 0, 0)
    keysSorted = sorted(observable.keys())
    while counter < 200:
        key = i % len(keysSorted)
        if observable[keysSorted[key]]:
            last = observable[keysSorted[key]].pop(0)
            counter += 1
        i += 1

    print(last[1]*100 + last[2])


main()
