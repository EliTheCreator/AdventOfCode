from collections import defaultdict


def main():
    with open("input", "r") as file:
        data = file.readline().strip()

    grid = defaultdict(lambda: ".", [((0, col), char)
                       for col, char in enumerate(data)])

    trapIndicators = ("^..", "^^.", ".^^", "..^")
    rows = 40
    cols = len(data)
    for row in range(1, rows):
        for col in range(cols):
            prevTiles = "".join((grid[(row - 1, col - 1)],
                                 grid[(row - 1, col)],
                                 grid[(row - 1, col + 1)]))
            if prevTiles in trapIndicators:
                grid[(row, col)] = "^"
            else:
                grid[(row, col)] = "."

    safeTiles = 0
    for row in range(rows):
        for col in range(cols):
            if grid[(row, col)] == ".":
                safeTiles += 1

    print(safeTiles)


if __name__ == "__main__":
    main()
