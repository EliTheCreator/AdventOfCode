import re
from collections import deque


def main():
    file = open("input", "r")
    p1_raw, p2_raw = file.read().split("\n\n")
    file.close()
    p1 = deque([int(x) for x in re.findall(r"\d+", p1_raw)][1:])
    p2 = deque([int(x) for x in re.findall(r"\d+", p2_raw)][1:])

    # counter = 1
    while p1 and p2:
        card_p1 = p1.popleft()
        card_p2 = p2.popleft()
        # print(f"-- Round {counter} --")
        # print(f"Player 1's deck: {p1}")
        # print(f"Player 2's deck: {p2}")
        # print(f"Player 1 plays: {card_p1}")
        # print(f"Player 2 plays: {card_p2}")
        if card_p1 > card_p2:
            # print("Player 1 wins the round!")
            p1.append(card_p1)
            p1.append(card_p2)
        elif card_p1 < card_p2:
            # print("Player 2 wins the round!")
            p2.append(card_p2)
            p2.append(card_p1)
        else:
            p1.append(card_p1)
            p2.append(card_p2)
        # counter += 1
        # print("")

    score = 0
    if p1:
        p1.reverse()
        for i, v in enumerate(p1, start=1):
            score += i * v
    else:
        p2.reverse()
        for i, v in enumerate(p2, start=1):
            score += i * v

    print(score)


if __name__ == "__main__":
    main()
