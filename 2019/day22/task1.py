import re
from collections import deque


def main():
    file = open("input", "r")
    tasks = []
    for line in file:
        line = line.strip().split()
        if line[0] == "deal":
            if line[1] == "into":
                tasks.append((0, 0))
            else:
                tasks.append((1, int(line[-1])))
        else:
            tasks.append((2, int(line[-1])))
    file.close()

    deckSize = 10007
    deck = deque(list(range(deckSize)))

    for task, count in tasks:
        if task == 0:
            deck.reverse()
        elif task == 1:
            newDeck = [0 for _ in range(deckSize)]
            pos = 0
            while deck:
                newDeck[pos] = deck.popleft()
                pos = (pos + count) % deckSize
            deck = deque(newDeck)
        elif task == 2:
            deck.rotate(count * -1)
        else:
            print(f"Error: Unknown task {task}")

    pos = 0
    while deck.popleft() != 2019:
        pos += 1
    print(pos)


if __name__ == "__main__":
    main()
