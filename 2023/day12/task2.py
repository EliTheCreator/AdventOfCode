
def get_num_arrangements(
    states: str,
    cur_length: int,
    lengths: tuple[int],
    min_length: int,
    in_dmgd: bool
) -> int:
    if (states, cur_length, lengths) in get_num_arrangements.cache:
        return get_num_arrangements.cache[(states, cur_length, lengths)]

    if min_length-cur_length > len(states):
        return 0

    if not states and not lengths:
        if in_dmgd:
            return 0
        else:
            return 1

    if not states and len(lengths)==1:
        return 1 if cur_length==lengths[0] else 0

    if not states and lengths:
        return 0

    cur, rem_states = (states[:1], states[1:])

    result = None
    match cur:
        case '?':
            result = get_num_arrangements('.'+rem_states, cur_length, lengths, min_length, in_dmgd) + \
                   get_num_arrangements('#'+rem_states, cur_length, lengths, min_length, in_dmgd)
        case '#':
            result = get_num_arrangements(rem_states, cur_length+1, lengths, min_length, True)
        case '.':
            if in_dmgd:
                if not lengths:
                    result = 0
                else:
                    target_length, rem_lengths = (None, None)
                    if len(lengths) == 1:
                        target_length = lengths[0]
                        rem_lengths = tuple()
                    else:
                        target_length, *rem_lengths = lengths
                        rem_lengths = tuple(rem_lengths)

                    if cur_length == target_length:
                        result = get_num_arrangements(rem_states, 0, rem_lengths, min_length-target_length, False)
                    else:
                        result = 0
            else:
                result = get_num_arrangements(rem_states, 0, lengths, min_length, False)
        case _:
            exit(-1)

    get_num_arrangements.cache[(states, cur_length, lengths)] = result

    return result


def main():
    with open("input", "r") as file:
        data = [line.strip().split(" ") for line in file.readlines()]

    rows = (
        (
            "?".join(symbols for _ in range(5)),
            5*[int(number) for number in numbers.split(",")]
        )
        for symbols, numbers in data
    )

    arrangements = 0
    for states, lengths in rows:
        get_num_arrangements.cache = {}
        arrangements += get_num_arrangements(states, 0, tuple(lengths), sum(lengths), False)

    print(arrangements)


if __name__ == "__main__":
    main()
