import re


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def main():
    with open("input", "r") as file:
        data = [[int(n) for n in re.findall(r"-?\d+", line)] for line in file.readlines()]
        beacons = [line[2:] for line in data]
        sensors = sorted([(line[:2], manhattan(*line)) for line in data], key=lambda line: line[0][0])

    targetY = 2000000

    noBeaconXs = set()
    for (x, y), manDist in sensors:
        if manhattan(x, y, x, targetY) > manDist:
            continue

        offset = 0
        while manhattan(x, y, x-offset, targetY) <= manDist:
            noBeaconXs.add(x - offset)
            noBeaconXs.add(x + offset)
            offset += 1

    beaconsOnTargetY = set([tuple(beacon) for beacon in beacons if beacon[1] == targetY])
    print(len(noBeaconXs) - len(beaconsOnTargetY))


if __name__ == "__main__":
    main()
