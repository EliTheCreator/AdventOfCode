import os
import re


def main():
    file = open("input", "r")
    floor = 0
    for i, s in enumerate(file.readline().strip()):
        if s == '(':
            floor += 1
        else:
            floor -= 1
            if floor < 0:
                print(i+1)
                break
    file.close()


if __name__ == "__main__":
    main()
