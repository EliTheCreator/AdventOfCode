from enum import IntEnum, auto
from itertools import combinations


class SpringState(IntEnum):
    Unknown = auto()
    Damaged = auto()
    Operational = auto()


def classify_symbol(symbol: str) -> SpringState:
    state: SpringState
    match symbol:
        case "?":
            state = SpringState.Unknown
        case "#":
            state = SpringState.Damaged
        case ".":
            state = SpringState.Operational
        case _:
            exit(1)

    return state


def main():
    with open("input", "r") as file:
        data = [line.strip().split(" ") for line in file.readlines()]

    rows = (
        (
            [classify_symbol(symbol) for symbol in symbols]+[SpringState.Operational],
            [int(number) for number in numbers.split(",")]
        )
        for symbols, numbers in data
    )

    arrangements_count = 0
    for states, lengths in rows:
        unknowns = 0
        damageds = 0
        for cur_state in states:
            match cur_state:
                case SpringState.Unknown:
                    unknowns += 1
                case SpringState.Damaged:
                    damageds += 1
                case SpringState.Operational:
                    pass

        damageds_needed = sum(lengths) - damageds

        for damaged_locations in combinations(range(unknowns), damageds_needed):
            unknowns_count = 0
            damaged_locations_index = 0
            in_damaged = False
            damaged_length = 0
            lengths_index = 0
            for state in states:
                cur_state: SpringState
                if state != SpringState.Unknown:
                    cur_state = state
                else:
                    if damaged_locations_index<len(damaged_locations) and unknowns_count == damaged_locations[damaged_locations_index]:
                        cur_state = SpringState.Damaged
                        damaged_locations_index += 1
                    else:
                        cur_state = SpringState.Operational
                    unknowns_count += 1

                match cur_state:
                    case SpringState.Operational:
                        if in_damaged:
                            if damaged_length != lengths[lengths_index]:
                                break
                            else:
                                in_damaged = False
                                damaged_length = 0
                                lengths_index += 1
                    case SpringState.Damaged:
                        if not in_damaged:
                            in_damaged = True
                        damaged_length += 1
                    case SpringState.Unknown:
                        exit(1)
            else:
                arrangements_count += 1

    print(arrangements_count)


if __name__ == "__main__":
    main()
