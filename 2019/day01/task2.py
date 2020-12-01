import os
import re


def main():
    file = open("input", "r")
    lines = [int(x) // 3 - 2 for x in file]
    file.close()

    sum = 0
    for x in lines:
        while x > 0:
            sum += x
            x = x // 3 - 2

    print(sum)


main()
