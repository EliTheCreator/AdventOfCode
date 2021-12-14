from collections import defaultdict


def main():
    with open("input", "r") as file:
        template, transitionsRaw = file.read().split("\n\n")

    transitions = dict((line.strip().split(" -> ")
                        for line in transitionsRaw.split("\n")))

    pairTransitions = {}
    for pair in set(transitions.keys()):
        middle = transitions[pair]
        pairTransitions[pair] = (pair[0] + middle, middle + pair[1])

    currentPairs = defaultdict(lambda: 0)
    for i in range(len(template) - 1):
        currentPairs[template[i:i+2]] += 1

    nextPairs = defaultdict(lambda: 0)

    letterCount = dict([(l, 0) for l in set(transitions.values())])
    for l in template:
        letterCount[l] += 1

    for _ in range(40):
        for pair, count in currentPairs.items():
            for nextPair in pairTransitions[pair]:
                nextPairs[nextPair] += count
            letterCount[transitions[pair]] += count

        currentPairs = nextPairs
        nextPairs = defaultdict(lambda: 0)

    print(max(letterCount.values()) - min(letterCount.values()))


if __name__ == "__main__":
    main()
