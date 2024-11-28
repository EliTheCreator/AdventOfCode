from collections import defaultdict, Counter
from enum import IntEnum, auto


class Type(IntEnum):
    HighCard = auto()
    OnePair = auto()
    TwoPair = auto()
    ThreeOfAKind = auto()
    FullHouse = auto()
    FourOfAKind = auto()
    FiveOfAKind = auto()


def assign_value(card: str) -> int:
    value: int
    match card:
        case "A":
            value = 14
        case "K":
            value = 13
        case "Q":
            value = 12
        case "J":
            value = 11
        case "T":
            value = 10
        case _:
            value = int(card)

    return value


def assign_type(binned_cards: dict[int, int]) -> Type:
    type: Type
    match len(binned_cards):
        case 1:
            type = Type.FiveOfAKind
        case 2:
            if 4 in binned_cards.values():
                type = Type.FourOfAKind
            else:
                type = Type.FullHouse
        case 3:
            if 3 in binned_cards.values():
                type = Type.ThreeOfAKind
            else:
                type = Type.TwoPair
        case 4:
            type = Type.OnePair
        case 5:
            type = Type.HighCard

    return type


def main():
    with open("input", "r") as file:
        data = [line.strip().split(" ") for line in file.readlines()]

    binned_hands: dict[Type, list[tuple[list[int], int]]] = defaultdict(lambda: list())
    for hand, bid in data:
        cards = [assign_value(card) for card in hand]
        binned_cards = Counter(cards)
        type = assign_type(binned_cards)
        binned_hands[type].append((cards, int(bid)))

    rank = 1
    total_winnings = 0
    for _, bin in sorted(list(binned_hands.items()), key=lambda pair: pair[0]):
        for _, bid in sorted(bin, key=lambda pair: pair[0]):
            total_winnings += bid*rank
            rank += 1

    print(total_winnings)


if __name__ == "__main__":
    main()
