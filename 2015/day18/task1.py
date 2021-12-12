from copy import deepcopy
from itertools import product


def main():
    with open("input", "r") as file:
        grid = [[False] + [False if c == '.' else True for c in line.strip()] + [False]
                for line in file.readlines()]

    cur = [[False for _ in range(len(grid[0]))]] + grid + \
        [[False for _ in range(len(grid[0]))]]
    next = deepcopy(cur)

    for _ in range(100):
        for row in range(1, len(cur) - 1):
            for col in range(1, len(cur[0]) - 1):
                neighboursOn = 0
                nextState = False
                for drow, dcol in product(range(-1, 2), repeat=2):
                    neighboursOn += cur[row + drow][col + dcol]
                if cur[row][col] and 3 <= neighboursOn and neighboursOn <= 4:
                    nextState = True
                elif not cur[row][col] and neighboursOn == 3:
                    nextState = True

                next[row][col] = nextState

        temp = cur
        cur = next
        next = temp

    print(sum((sum(row) for row in cur)))


if __name__ == "__main__":
    main()
