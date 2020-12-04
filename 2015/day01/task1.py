import os
import re


def main():
    file = open("input", "r")
    floor = 0
    for s in file.readline().strip():
        if s == '(':
            floor += 1
        else:
            floor -= 1
    file.close()

    print(floor)


if __name__ == "__main__":
    main()
