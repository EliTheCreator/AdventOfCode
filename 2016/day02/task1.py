

def main():
    with open("input", "r") as file:
        instrucions = [line.strip() for line in file.readlines()]

    numpad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    row, col = 1, 1

    code = []
    for instrucion in instrucions:
        for letter in instrucion:
            match letter:
                case "U":
                    if row > 0:
                        row -= 1
                case "D":
                    if row < 2:
                        row += 1
                case "L":
                    if col > 0:
                        col -= 1
                case "R":
                    if col < 2:
                        col += 1
                case _:
                    pass

        code.append(numpad[row][col])

    print("".join((str(x) for x in code)))


if __name__ == "__main__":
    main()
