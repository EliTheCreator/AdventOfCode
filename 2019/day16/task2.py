import re


def main():
    file = open("input", "r")
    sequence = [int(x) for x in re.findall(r"\d", file.readline())] + [0]
    file.close()

    # outFile = open("output", "w")

    pattern = [0, 1, 0, -1]

    # for _ in range(100):
    #     newSeqence = [0 for _ in range(len(sequence))]

    #     for i in range(len(sequence)//2, len(sequence) - 1)[::-1]:
    #         newSeqence[i] = sequence[i] + newSeqence[i + 1]

    #     for j in range(1, len(sequence) + 1):
    #         # for i, num in enumerate(sequence):
    #         i = 0
    #         while i < len(sequence):
    #             num = sequence[i]
    #             patternIndex = ((i+1)//j) % 4
    #             if pattern[patternIndex] != 0:
    #                 newSeqence[j-1] += num * pattern[patternIndex]
    #                 i += 1
    #             else:
    #                 # print("jump")
    #                 # print(i)
    #                 i += j

    #     for i, num in enumerate(newSeqence):
    #         newSeqence[i] = abs(num) % 10
    #     sequence = newSeqence

    # print("".join([str(x) for x in sequence[:8]]))

    for j in range(1, len(sequence) + 1):
        for i in range(len(sequence)):
            print(pattern[((i+1)//j) % 4], end='')
            # outFile.write(str(pattern[((i+1)//j) % 4]))
        print("")
        # outFile.write("\n")


if __name__ == "__main__":
    main()
