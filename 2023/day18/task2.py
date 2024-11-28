
def main():
    with open("input", "r") as file:
        data = [line.strip().split(" ") for line in file.readlines()]

    up = (-1, 0)
    down = (1, 0)
    left = (0, -1)
    right = (0, 1)

    row, col = (0,0)
    inner_area = 0
    border = 0
    for _, _, color in data:
        distance = int(color[2:7], 16)
        match color[7]:
            case "0":
                d_row, d_col = right
            case "1":
                d_row, d_col = down
            case "2":
                d_row, d_col = left
            case "3":
                d_row, d_col = up

        border += distance
        next_row = row + distance*d_row
        next_col = col + distance*d_col

        # shoelace trapezoid  formula
        inner_area += (row+next_row)*(col-next_col)

        row = next_row
        col = next_col

    # pick's theorem
    inner_area = abs(inner_area+border)//2 + 1
    print(inner_area)


if __name__ == "__main__":
    main()
