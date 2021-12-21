from collections import Counter
from functools import cache
from itertools import product
from re import findall


def main():
    with open("input", "r") as file:
        startPosP1, startPosP2 = [int(findall(r"\d+", line)[-1])
                                  for line in file.readlines()]

    winningScore = 21
    boardSpaces = 10
    dieSides = 3
    throws = 3

    dieSums = list(Counter((sum(permutation) for permutation in product(
        range(1, dieSides + 1), repeat=throws))).items())

    @cache
    def move(posP1, posP2, scoreP1, scoreP2):
        if scoreP2 >= winningScore:
            return 0, 1

        winsP1, winsP2 = 0, 0
        for dieSum, n in dieSums:
            nextPosP1 = (posP1 + dieSum) % boardSpaces or boardSpaces
            dWinsP2, dWinsP1 = move(
                posP2, nextPosP1, scoreP2, scoreP1 + nextPosP1)
            winsP1 += n * dWinsP1
            winsP2 += n * dWinsP2

        return winsP1, winsP2

    print(max(move(startPosP1, startPosP2, 0, 0)))


if __name__ == "__main__":
    main()
