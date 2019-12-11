from collections import deque
import re

def main():
    file = open("input", "r")
    players, lastMarble = [int(x) for x in re.findall("[0-9]+", file.readline())]
    file.close()

    circle = deque([0])
    currentPlayer = 0
    tally = [0 for _ in range(players)]

    for i in range(1, (lastMarble * 100) + 1):
        if i % 23:
            circle.rotate(-1)
            circle.append(i)
        else:
            circle.rotate(7)
            tally[currentPlayer] += i + circle.pop()
            circle.rotate(-1)

        currentPlayer = (currentPlayer + 1) % players

    print(max(tally))

main()