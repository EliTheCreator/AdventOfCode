

def main():
    with open("input", "r") as file:
        initialValue = int(file.readline().strip())

    previousWinner = 0
    for round in range(2, initialValue + 1):
        loser = round // 2
        winner = 1 + previousWinner
        if winner >= loser:
            winner += 1
            winner %= round
        previousWinner = winner


if __name__ == "__main__":
    main()
