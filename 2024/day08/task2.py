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
                antinodes.add((row, col))
                scalar = 1
                while True:
                    nrow = row + mul*scalar*drow
                    ncol = col + mul*scalar*dcol
                    
                    if nrow<0 or num_rows<=nrow or ncol<0 or num_cols<=ncol:
                        break

                    antinodes.add((nrow, ncol))
                    scalar += 1

    print(len(antinodes))


if __name__ == "__main__":
    main()
