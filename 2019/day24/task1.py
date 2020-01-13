
def main():
    file = open("input", "r")
    layout = [[" " for _ in range(7)] for _ in range(7)]
    for y, line in enumerate(file):
        for x, space in enumerate(line.strip("\n")):
            if space == "#":
                layout[y+1][x+1] = space
            else:
                layout[y+1][x+1] = " "

    file.close()

    ratings = set()

    rating = 0
    for y in range(1, 6):
        for x in range(1, 6):
            if layout == "#":
                rating += 1 << (y-1) * 5 + (x-1)

    ratings.add(rating)

    while True:
        newLayout = [[" " for _ in range(7)] for _ in range(7)]
        for y in range(1, 6):
            for x in range(1, 6):
                neighbours = 0
                for ny, nx in ((y-1, x), (y+1, x), (y, x-1), (y, x+1)):
                    if layout[ny][nx] == "#":
                        neighbours += 1

                if layout[y][x] == "#":
                    if neighbours == 1:
                        newLayout[y][x] = "#"
                    else:
                        newLayout[y][x] = " "
                else:
                    if neighbours == 1 or neighbours == 2:
                        newLayout[y][x] = "#"
                    else:
                        newLayout[y][x] = " "

        layout = newLayout

        rating = 0
        for y in range(1, 6):
            for x in range(1, 6):
                if layout[y][x] == "#":
                    rating += 1 << (y-1) * 5 + (x-1)

        if rating in ratings:
            print(rating)
            break
        else:
            ratings.add(rating)


if __name__ == "__main__":
    main()
