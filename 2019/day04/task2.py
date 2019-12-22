import re


def main():
    file = open("input", "r")
    mmin, mmax, *_ = [int(x) for x in re.findall(r"\d+", file.readline())]
    file.close()

    count = 0
    for num in range(mmin, mmax + 1):
        array = [int(x) for x in str(num)]
        containsAdjacent = [False] + [array[i] == array[i+1]
                                      for i in range(len(array) - 1)] + [False]
        onlyPair = any([containsAdjacent[i] == False and containsAdjacent[i+1] ==
                        True and containsAdjacent[i+2] == False for i in range(len(containsAdjacent) - 2)])
        decreasing = any([array[i] > array[i+1]
                          for i in range(len(array) - 1)])

        if containsAdjacent and onlyPair and not decreasing:
            count += 1

    print(count)


main()
