import re


def main():
    with open("input", "r") as file:
        draws = [int(x) for x in re.findall("[0-9]+", file.readline())]
        file.readline()

        size = 5
        cards = [([0 for _ in range(size + size)], [False for _ in range(size * size)], [int(x) for x in re.findall("[0-9]+", card)])
                 for card in file.read().split("\n\n")]

    filtered_cards = cards
    for draw in draws:
        filtered_cards_temp = []
        for (totals, marked, card) in filtered_cards:
            add_to_filtered = True

            def gen():
                for row in range(size):
                    for col in range(size):
                        yield (row, col)

            for (row, col) in gen():
                if card[row * size + col] == draw:
                    marked[row * size + col] = True
                    totals[row] += 1
                    totals[size + col] += 1

                    if totals[row] == size or totals[size + col] == size:
                        if len(filtered_cards) == 1:
                            print(
                                draw * sum([x for (m, x) in zip(marked, card) if not m]))
                            return
                        else:
                            add_to_filtered = False

            if add_to_filtered:
                filtered_cards_temp.append((totals, marked, card))

        filtered_cards = filtered_cards_temp


if __name__ == "__main__":
    main()
