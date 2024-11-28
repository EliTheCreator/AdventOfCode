
def main():
    with open("input", "r") as file:
        trees = [[int(x) for x in line.strip()] for line in file.readlines()]
        height = len(trees)
        width = len(trees[0])

    topScenicScore = 0

    for y in range(1, height-1):
        for x in range(1, width-1):
            curHeight = trees[y][x]
            curScenicScore = 1

            directionalScenicScore = 0
            for dy in range(y-1, -1, -1):
                directionalScenicScore += 1
                if trees[dy][x] >= curHeight:
                    break
            curScenicScore *= directionalScenicScore

            directionalScenicScore = 0
            for dy in range(y+1, height):
                directionalScenicScore += 1
                if trees[dy][x] >= curHeight:
                    break
            curScenicScore *= directionalScenicScore

            directionalScenicScore = 0
            for dx in range(x-1, -1, -1):
                directionalScenicScore += 1
                if trees[y][dx] >= curHeight:
                    break
            curScenicScore *= directionalScenicScore

            directionalScenicScore = 0
            for dx in range(x+1, width):
                directionalScenicScore += 1
                if trees[y][dx] >= curHeight:
                    break
            curScenicScore *= directionalScenicScore

            if curScenicScore > topScenicScore:
                topScenicScore = curScenicScore

    print(topScenicScore)



if __name__ == "__main__":
    main()
