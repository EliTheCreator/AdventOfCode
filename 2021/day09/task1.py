from collections import defaultdict
import re


def main():
    heightmap = defaultdict(lambda: 9, [])

    candidates = []
    with open("input", "r") as file:
        for (x, line) in enumerate(file.readlines(), 1):
            prev = 1
            cur = 0
            line = line.strip() + "9"
            for (y, level_raw) in enumerate(re.findall("[0-9]", line), 1):
                level = int(level_raw)
                heightmap[(x, y)] = level
                prev += heightmap[(x, y-1)] < level
                if prev == 2:
                    candidates.append((x, y-1))

                cur += heightmap[(x, y-1)] > level
                prev = cur
                cur = 0

    risk_level = 0
    for (x, y) in candidates:
        level = heightmap[(x, y)]
        if heightmap[(x-1, y)] > level and heightmap[(x+1, y)] > level:
            risk_level += 1 + level

    print(risk_level)


if __name__ == "__main__":
    main()
