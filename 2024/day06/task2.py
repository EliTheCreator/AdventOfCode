from itertools import product


def main():
    with open("input", "r") as file:
        _map = ["X" + line.strip() + "X" for line in file.readlines()]
        _map = ["X"*len(_map[0])] + _map + ["X"*len(_map[0])]

    srow, scol = 0, 0
    for srow in range(len(_map)):
        found = False
        for scol in range(len(_map)):
            if _map[srow][scol]  == "^":
                found = True
                break
        if found:
            break

    loops = 0
    directions = ((-1,0),(0,1),(1,0),(0,-1))
    for trow, tcol in product(range(1, len(_map)-1), range(1, len(_map[0])-1)):
        if _map[trow][tcol] in "X#^":
            continue

        row, col = srow, scol
        visited = set()
        direction = 0
        while True:
            drow, dcol = directions[direction]
            if (row, col, drow, dcol) in visited:
                loops += 1
                break
            visited.add((row, col, drow, dcol))

            if (trow, tcol) == (row+drow, col+dcol):
                direction = (direction+1)%len(directions)
                continue
            match _map[row+drow][col+dcol]:
                case '.' | '^':
                    row += drow
                    col += dcol
                case '#':
                    direction = (direction+1)%len(directions)
                case 'X':
                    break

    print(loops)


if __name__ == "__main__":
    main()
