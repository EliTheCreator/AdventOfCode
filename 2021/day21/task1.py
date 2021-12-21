import re


def main():
    with open("input", "r") as file:
        posP1, posP2 = [int(line.strip()[-1]) - 1 for line in file.readlines()]

    scoreP1, scoreP2 = 0, 0
    turn = 0
    die = 1

    while scoreP1 < 1000 and scoreP2 < 1000:
        turn += 1
        dieSum = sum(((x - 1) % 100) + 1 for x in range(die, die + 3))
        die = ((die + 2) % 100) + 1
        if turn % 2:
            posP1 = (posP1 + dieSum) % 10
            scoreP1 += posP1 + 1
        else:
            posP2 = (posP2 + dieSum) % 10
            scoreP2 += posP2 + 1

    if scoreP1 >= 1000:
        print(scoreP2 * turn * 3)
    else:
        print(scoreP1 * turn * 3)


if __name__ == "__main__":
    main()
