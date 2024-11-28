from functools import reduce
import re


def main():
    with open("input", "r") as file:
        sequences = [[int(x) for x in re.findall(r"-?\d+", line)] for line in file.readlines()]

    result = 0
    for sequence in sequences:
        last_elems = []
        while any(x!=0 for x in sequence):
            last_elems.append(sequence[-1])
            new_sequence = []
            for first, second in zip(sequence, sequence[1:]):
                new_sequence.append(second-first)

            sequence = new_sequence

        last_elems.append(sequence[-1])

        result += reduce(lambda b, a: a+b, reversed(last_elems))

    print(result)


if __name__ == "__main__":
    main()
