import re


def main():
    file = open("input", "r")
    mmin, mmax, *_ = [int(x) for x in re.findall(r"\d+", file.readline())]
    file.close()

    count = 0
    for num in range(mmin, mmax + 1):
        array = [int(x) for x in str(num)]
        containsAdjacent = any([array[i] == array[i+1]
                                for i in range(len(array) - 1)])
        decreasing = any([array[i] > array[i+1]
                          for i in range(len(array) - 1)])

        if containsAdjacent and not decreasing:
            count += 1

    print(count)


main()
