

def main():
    file = open("input", "r")
    puzzleInput = int(file.readline().strip())
    file.close()

    scoreBoard = [3, 7]
    firstElfPos = 0
    secondElfPos = 1

    for _ in range(100000000):
        firstElfRecipeScore = scoreBoard[firstElfPos]
        secondElfRecipeScore = scoreBoard[secondElfPos]
        newRecipe = firstElfRecipeScore + secondElfRecipeScore
        if newRecipe > 9:
            scoreBoard.append(newRecipe // 10)
            scoreBoard.append(newRecipe % 10)
        else:
            scoreBoard.append(newRecipe)

        boardSize = len(scoreBoard)

        firstElfPos = (firstElfPos + firstElfRecipeScore + 1) % boardSize
        secondElfPos = (secondElfPos + secondElfRecipeScore + 1) % boardSize

    key = []
    num = puzzleInput
    while num > 0:
        key.append(num % 10)
        num = num // 10

    key.reverse()

    def compare(start):
        for i in range(len(key)):
            if scoreBoard[start+i] != key[i]:
                return False
        return True

    for i in range(len(scoreBoard)-len(key)):
        if compare(i):
            print(i)
            break


if __name__ == "__main__":
    main()
