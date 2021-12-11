from itertools import count
import re


def main():
    size = 10
    grid = [[-1 for _ in range(size + 2)] for _ in range(size + 2)]
    with open("input", "r") as file:
        for row, line in enumerate(file.readlines(), 1):
            for col, level in enumerate(re.findall("[0-9]", line), 1):
                grid[row][col] = int(level)

    neighbours_offset = frozenset([(-1, -1), (-1, 0), (-1, 1),
                                  (0, -1),           (0, 1),
                                  (1, -1),  (1, 0),  (1, 1), ])

    for step in count(1):
        has_flashed = []
        neighbours = []
        for row in range(1, size + 1):
            for col in range(1, size + 1):
                grid[row][col] += 1
                if grid[row][col] == 10:
                    has_flashed.append((row, col))
                    for dr, dc in neighbours_offset:
                        neighbours.append((row + dr, col + dc))

        while neighbours:
            row, col = neighbours.pop()
            if grid[row][col] > -1:
                grid[row][col] += 1
                if grid[row][col] == 10:
                    has_flashed.append((row, col))
                    for dr, dc in neighbours_offset:
                        neighbours.append((row + dr, col + dc))

        if len(has_flashed) == size * size:
            print(step)
            break
        for row, col in has_flashed:
            grid[row][col] = 0


if __name__ == "__main__":
    main()
