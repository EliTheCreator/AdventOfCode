import re


def main():
    file = open("input", "r")
    sequence = [int(x) for x in re.findall(r"\d", file.readline())]
    file.close()

    seqLength = len(sequence)
    offset = int("".join(str(x) for x in sequence[:7]))

    sequence = sequence[offset % seqLength:] + \
        (10000 - (offset//seqLength) - 1) * sequence + [0]

    for _ in range(100):
        newSeqence = [0 for _ in range(len(sequence))]

        for i in reversed(range(len(sequence) - 1)):
            newSeqence[i] = sequence[i] + newSeqence[i + 1]

        for i in range(seqLength):
            newSeqence[i] %= 10

        sequence = newSeqence

    print("".join(str(x) for x in sequence[:8]))


if __name__ == "__main__":
    main()
