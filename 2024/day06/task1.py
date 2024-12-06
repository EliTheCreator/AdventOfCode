
def main():
    with open("input", "r") as file:
        _map = ["X" + line.strip() + "X" for line in file.readlines()]
        _map = ["X"*len(_map[0])] + _map + ["X"*len(_map[0])]

    row, col = 0, 0
    for row in range(len(_map)):
        found = False
        for col in range(len(_map)):
            if _map[row][col]  == "^":
                found = True
                break
        if found:
            break

    directions = ((-1,0),(0,1),(1,0),(0,-1))
    visited = set()
    direction = 0
    while True:
        visited.add((row, col))
        drow, dcol = directions[direction]
        match _map[row+drow][col+dcol]:
            case '.' | '^':
                row += drow
                col += dcol
            case '#':
                direction = (direction+1)%len(directions)
            case 'X':
                break

    print(len(visited))


if __name__ == "__main__":
    main()
