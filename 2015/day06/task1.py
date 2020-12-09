import os
import re


def main():
    file = open("input", "r")
    commands = [(re.findall(r"toggle|on|off", line)[0], [int(x)
                                                         for x in re.findall(r"[0-9]+", line)]) for line in file.readlines()]

    lights = [[False for _ in range(1000)] for _ in range(1000)]

    for command, (x1, y1, x2, y2) in commands:
        if command == "toggle":
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    lights[x][y] = not lights[x][y]
        elif command == "on":
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    lights[x][y] = True
        if command == "off":
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    lights[x][y] = False

    print(sum([len(list(filter(None, x))) for x in lights]))


if __name__ == "__main__":
    main()
