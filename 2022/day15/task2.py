import re


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def main():
    with open("input", "r") as file:
        data = [[int(n) for n in re.findall(r"-?\d+", line)] for line in file.readlines()]
        sensors = sorted([(line[:2], manhattan(*line)) for line in data], key=lambda line: line[0][0])

    maxVal = 4000000
    for y in range(maxVal+1):
        x = 0
        while x <= maxVal:
            for  (sensorX, sensorY), manDist in sensors:
                if manhattan(x, y, sensorX, sensorY) <= manDist:
                    x = sensorX + manDist - abs(y - sensorY) + 1
                    break
            else:
                print(x*4000000 + y)
                return


if __name__ == "__main__":
    main()
