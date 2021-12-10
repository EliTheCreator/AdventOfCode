from collections import defaultdict
from functools import reduce
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

    low_points = []
    for (x, y) in candidates:
        level = heightmap[(x, y)]
        if heightmap[(x-1, y)] > level and heightmap[(x+1, y)] > level:
            low_points.append((x, y))

    sizes = []
    for low_point in low_points:
        size = 0
        queue = [low_point]
        visited = set()
        while queue:
            x, y = queue.pop(0)
            if (x, y) not in visited:
                visited.add((x, y))
                size += 1
                level = heightmap[(x, y)]
                for (dx, dy) in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                    neighbour = (x+dx, y+dy)
                    neighbour_level = heightmap[neighbour]
                    if level < neighbour_level and neighbour_level < 9:
                        queue.append(neighbour)

        sizes.append(size)

    print(reduce((lambda a, b: a*b), sorted(sizes)[-3:]))


if __name__ == "__main__":
    main()
