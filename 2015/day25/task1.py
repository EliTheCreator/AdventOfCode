from itertools import count
import re


def main():
    with open("input", "r") as file:
        data = [int(x) for x in re.findall(r"\d+", file.readline())]

    targetRow, targetColumn = data

    code = 20151125
    multiplier = 252533
    divisor = 33554393

    for start in count(2):
        row = start
        column = 1
        while row >= 1:
            code = (code * multiplier) % divisor
            if row == targetRow and column == targetColumn:
                print(code)
                return
            row -= 1
            column += 1


if __name__ == "__main__":
    main()
