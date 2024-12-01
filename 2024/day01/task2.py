from collections import Counter


def main():
    with open("input", "r") as file:
        data = [
            [int(elem) for elem in line.strip().split("   ")]
            for line in file.readlines()
        ]

    similarity_score = 0
    first, second = list(sorted(elem) for elem in zip(*data))
    first = set(first)
    second = Counter(second)

    for val in first:
        if val not in second:
            continue

        similarity_score += val * second[val]

    print(similarity_score)


if __name__ == "__main__":
    main()
