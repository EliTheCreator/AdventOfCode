from collections import deque
from re import findall


def main():
    with open("input", "r") as file:
        instrs = [line.strip().split(" ") for line in file.readlines()]

    grid = [deque([False for _ in range(50)]) for _ in range(6)]

    for instr in instrs:
        match instr:
            case "rect", dimensions:
                dx, dy = (int(num) for num in findall(r"\d+", dimensions))
                for y in range(dy):
                    for x in range(dx):
                        grid[y][x] = True
            case "rotate", rowOrColumn, *dimensions:
                rc, amount = (int(num)
                              for num in findall(r"\d+", "".join(dimensions)))
                if rowOrColumn == "row":
                    grid[rc].rotate(amount)
                if rowOrColumn == "column":
                    col = deque([grid[row][rc] for row in range(len(grid))])
                    col.rotate(amount)
                    for row in range(len(grid)):
                        grid[row][rc] = col[row]
            case _:
                pass

    print(sum((sum(line) for line in grid)))


if __name__ == "__main__":
    main()
