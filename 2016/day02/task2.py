

def main():
    with open("input", "r") as file:
        instrucions = [line.strip() for line in file.readlines()]

    numpad = [["0", "0", "1", "0", "0"],
              ["0", "2", "3", "4", "0"],
              ["5", "6", "7", "8", "9"],
              ["0", "A", "B", "C", "0"],
              ["0", "0", "D", "0", "0"]]
    row, col = 0, -2

    code = []
    for instrucion in instrucions:
        for letter in instrucion:
            match letter:
                case "U":
                    if abs(row - 1) + abs(col) < 3:
                        row -= 1
                case "D":
                    if abs(row + 1) + abs(col) < 3:
                        row += 1
                case "L":
                    if abs(row) + abs(col - 1) < 3:
                        col -= 1
                case "R":
                    if abs(row) + abs(col + 1) < 3:
                        col += 1
                case _:
                    pass

        code.append(numpad[row + 2][col + 2])

    print("".join((x for x in code)))


if __name__ == "__main__":
    main()
