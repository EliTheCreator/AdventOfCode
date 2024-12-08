from collections import defaultdict
from itertools import combinations


def main():
    num_rows = 0
    num_cols = 0
    antennas = defaultdict(lambda: set())
    with open("input", "r") as file:
        for row, line in enumerate(file.readlines()):
            num_rows = row + 1
            for col, frequency in enumerate(line.strip()):
                num_cols = col + 1
                if frequency == '.':
                    continue

                antennas[frequency].add((row, col))

    antinodes = set()
    for locations in antennas.values():
        for combination in combinations(locations, 2):
            combination = sorted(combination, key=lambda position: position[0])

            (row1, col1), (row2, col2) = combination
            drow = (row2-row1)
            dcol = (col2-col1)
            for (row, col), mul in zip(combination, (-1, 1)):
                nrow = row + mul*drow
                ncol = col + mul*dcol
                
                if 0 <= nrow < num_rows and 0 <= ncol < num_cols:
                    antinodes.add((nrow, ncol))

    print(len(antinodes))


if __name__ == "__main__":
    main()
