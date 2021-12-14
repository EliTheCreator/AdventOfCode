from collections import Counter


def main():
    with open("input", "r") as file:
        template, transitionsRaw = file.read().split("\n\n")

    transitions = dict((line.strip().split(" -> ")
                        for line in transitionsRaw.split("\n")))
    letters = Counter(template)
    pairs = Counter(map(lambda x: x[0] + x[1], zip(template, template[1:])))

    for _ in range(40):
        nextPairs = Counter("")
        for (left, right), count in pairs.items():
            middle = transitions[left + right]
            letters[middle] += count
            nextPairs[left + middle] += count
            nextPairs[middle + right] += count
        pairs = nextPairs

    print(max(letters.values()) - min(letters.values()))


if __name__ == "__main__":
    main()
