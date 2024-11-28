from itertools import combinations


def main():
    with open("input", "r") as file:
        universe = [line.strip() for line in file.readlines()]

    rows = set(x for x in range(len(universe)))
    cols = set(x for x in range(len(universe[0])))

    galaxies: list[tuple[int, int]] = []
    for row, line in enumerate(universe):
        for col, letter in enumerate(line):
            if letter=="#":
                galaxies.append((row, col))
                rows.discard(row)
                cols.discard(col)

    lengths = 0
    for (f_row, f_col), (s_row, s_col) in combinations(galaxies, 2):
        f_col, s_col = (f_col, s_col) if f_col<s_col else (s_col, f_col)

        row_diff = s_row-f_row
        for row in rows:
            if f_row < row < s_row:
                row_diff += 1

        col_diff = s_col-f_col
        for col in cols:
            if f_col < col < s_col:
                col_diff += 1

        lengths += row_diff + col_diff

    print(lengths)


if __name__ == "__main__":
    main()
