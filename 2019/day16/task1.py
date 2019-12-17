import re


def main():
    file = open("input", "r")
    sequence = [int(x) for x in re.findall(r"\d", file.readline())]
    file.close()

    pattern = [0, 1, 0, -1]

    for _ in range(100):
        newSeqence = [0 for _ in range(len(sequence))]

        for j in range(1, len(sequence) + 1):
            for i, num in enumerate(sequence):
                patternIndex = ((i+1)//j) % 4
                newSeqence[j-1] += num * pattern[patternIndex]

        for i, num in enumerate(newSeqence):
            newSeqence[i] = abs(num) % 10
        sequence = newSeqence

    print("".join([str(x) for x in sequence[:8]]))

    # for j in range(1, 9):
    #     for i in range(8):
    #         print(pattern[((i+1)//j) % 4], end='')
    #     print("")


if __name__ == "__main__":
    main()
