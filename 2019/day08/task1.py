import re


def main():
    file = open("input", "r")
    data = [int(x) for x in re.findall("[0-9]", file.readline())]
    file.close()

    size = 25 * 6
    minZeros = size
    maxOnes = 0
    maxTwos = 0

    for i in range(0, len(data), size):
        zeros = 0
        ones = 0
        twos = 0
        for j in range(size):
            if data[i + j] == 0:
                zeros += 1
            elif data[i + j] == 1:
                ones += 1
            else:
                twos += 1

        if minZeros > zeros:
            minZeros = zeros
            maxOnes = ones
            maxTwos = twos

    print(maxOnes * maxTwos)


main()
