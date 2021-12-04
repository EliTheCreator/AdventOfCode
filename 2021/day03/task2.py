import functools
import re


def filter_data(data, op):
    pos = 0
    filtered = data
    while True:
        votes_for_one = sum([row[pos] for row in filtered])
        majority = len(filtered)/2
        criteria_bit = 1 if op(votes_for_one, majority) else 0

        filtered_temp = []
        for row in filtered:
            if row[pos] == criteria_bit:
                filtered_temp.append(row)

        pos += 1
        filtered = filtered_temp

        if len(filtered) == 1:
            break

    return int("".join([str(x) for x in filtered[0]]), 2)


def main():
    with open("input", "r") as file:
        data = [[int(x) for x in re.findall("[01]", line)]
                for line in file.readlines()]

    sums = functools.reduce(lambda x, y: [a + b for (a, b) in zip(x, y)], data)

    oxygen_generator_rating = filter_data(data, lambda x, y: x >= y)
    co2_scrubber_rating = filter_data(data, lambda x, y: x < y)

    print(oxygen_generator_rating * co2_scrubber_rating)


if __name__ == "__main__":
    main()
