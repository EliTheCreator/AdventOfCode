
def main():
    with open("input", "r") as file:
        trees = [[int(x) for x in line.strip()] for line in file.readlines()]
        height = len(trees)
        width = len(trees[0])

    visible = set()

    for x in range(width):
        curMax = -1
        for y in range(height):
            if trees[y][x] > curMax:
                visible.add((x,y))
                curMax = trees[y][x]
                if curMax == 9:
                    break

    for x in range(width-1, -1, -1):
        curMax = -1
        for y in range(height-1, -1, -1):
            if trees[y][x] > curMax:
                visible.add((x,y))
                curMax = trees[y][x]
                if curMax == 9:
                    break

    for y in range(height):
        curMax = -1
        for x in range(width):
            if trees[y][x] > curMax:
                visible.add((x,y))
                curMax = trees[y][x]
                if curMax == 9:
                    break

    for y in range(height-1, -1, -1):
        curMax = -1
        for x in range(width-1, -1, -1):
            if trees[y][x] > curMax:
                visible.add((x,y))
                curMax = trees[y][x]
                if curMax == 9:
                    break

    print(len(visible))



if __name__ == "__main__":
    main()
