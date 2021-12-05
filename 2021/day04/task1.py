import re


def main():
    with open("input", "r") as file:
        draws = [int(x) for x in re.findall("[0-9]+", file.readline())]
        file.readline()

        size = 5
        cards = [([0 for _ in range(size + size)], [False for _ in range(size * size)], [int(x) for x in re.findall("[0-9]+", card)])
                 for card in file.read().split("\n\n")]

    for draw in draws:
        for (totals, marked, card) in cards:
            for row in range(size):
                for col in range(size):
                    if card[row * size + col] == draw:
                        marked[row * size + col] = True
                        totals[row] += 1
                        totals[size + col] += 1

                        if totals[row] == 5 or totals[size + col] == 5:
                            print(
                                draw * sum([x for (m, x) in zip(marked, card) if not m]))
                            return


if __name__ == "__main__":
    main()
