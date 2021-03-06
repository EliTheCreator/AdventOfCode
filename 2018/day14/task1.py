

def main():
    file = open("input", "r")
    minRecipes = int(file.readline().strip())
    file.close()

    scoreBoard = [3, 7]
    firstElfPos = 0
    secondElfPos = 1

    for _ in range(minRecipes):
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

    for c in scoreBoard[minRecipes:minRecipes+10]:
        print(c, end="")

    print("")


if __name__ == "__main__":
    main()
