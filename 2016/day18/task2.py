

def main():
    with open("input", "r") as file:
        firstLine = "".join(
            ["1" if char == "^" else "0" for char in file.readline().strip()])

    lines = {int(firstLine, 2): 0, }
    safes = {0: sum((1 if char == "0" else 0 for char in firstLine)), }
    first = 0

    trapIndicators = ("100", "110", "011", "001")
    cols = len(firstLine)
    row = 0
    prevLine = "0" + firstLine + "0"
    while row < 400000:
        row += 1
        curLine = []
        for col in range(cols):
            prevTiles = prevLine[col:col+3]
            tile = "1" if prevTiles in trapIndicators else "0"
            curLine.append(tile)

        curLine = "".join(curLine)
        curLineVal = int(curLine, 2)
        if curLineVal in lines.keys():
            first = lines[curLineVal]
            break

        lines[curLineVal] = row
        safes[row] = sum(
            (1 if char == "0" else 0 for char in curLine))
        prevLine = "0" + curLine + "0"
    else:
        totalSum = 0
        for curRow in range(400000):
            totalSum += safes[curRow]
        print(totalSum)
        return

    sumPrevious = 0
    for curRow in range(0, first):
        sumPrevious += safes[curRow]

    sumPattern = 0
    for curRow in range(first, row):
        sumPattern += safes[curRow]

    patSize = row - first
    repetitions = (400000 - first) // patSize
    leftover = (400000 - first) % patSize

    sumLeftover = 0
    for curRow in range(first, first + leftover):
        sumLeftover += safes[curRow]

    print(sumPrevious + repetitions * sumPattern + sumLeftover)


if __name__ == "__main__":
    main()
