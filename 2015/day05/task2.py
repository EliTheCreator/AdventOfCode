import os
import re


def main():
    file = open("input", "r")
    strings = [x.strip() for x in file.readlines()]
    file.close()

    print(len([s for s in strings if (re.search(r"(..).*\1", s) and
                                      re.search(r"(.).\1", s))]))


if __name__ == "__main__":
    main()
