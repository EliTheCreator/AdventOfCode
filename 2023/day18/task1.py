from collections import defaultdict


def main():
    with open("input", "r") as file:
        data = [line.strip().split(" ") for line in file.readlines()]

    up = (-1, 0)
    down = (1, 0)
    left = (0, -1)
    right = (0, 1)


    row, min_row, max_row = 0, 0, 0
    col, min_col, max_col = 0, 0, 0
    lagoon = defaultdict(lambda: False)
    lagoon[(row, col)] = True
    for direction, distance, _ in data:
        match direction:
            case "U":
                drow, dcol = up
            case "D":
                drow, dcol = down
            case "L":
                drow, dcol = left
            case "R":
                drow, dcol = right

        for _ in range(int(distance)):
            row += drow
            col += dcol
            min_row, max_row = min(min_row, row), max(max_row, row)
            min_col, max_col = min(min_col, col), max(max_col, col)
            lagoon[(row, col)] = True

    min_row -= 1
    max_row += 1
    min_col -= 1
    max_col += 1
    stack = [(min_row, min_col)]
    visited = set()
    while stack:
        row, col = stack.pop()

        if lagoon[(row, col)]:
            continue

        visited.add((row, col))

        for drow, dcol in (up, down, left, right):
            nrow = row+drow
            ncol = col+dcol

            if nrow<min_row or max_row<nrow or ncol<min_col or max_col<ncol:
                continue

            if (nrow, ncol) in visited:
                continue

            stack.append((nrow, ncol))

    print((max_row-(min_row-1))*(max_col-(min_col-1)) - len(visited))


if __name__ == "__main__":
    main()
