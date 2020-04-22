import os
import re


def main():
    file = open("input", "r")
    lines = [int(x) for x in file]

    totSum = 0
    for x in lines:
        x = x // 3 - 2
        while x > 0:
            totSum += x
            x = x // 3 - 2
    file.close()

    print(totSum)


main()
