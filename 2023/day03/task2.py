from collections import defaultdict
from enum import IntEnum, auto
from functools import reduce
from itertools import product
from string import digits


class Category(IntEnum):
    Digit = auto()
    Asterisk = auto()
    Other = auto()


def categorize_letter(letter) -> Category:
    letter_category: Category
    if letter in digits:
        letter_category = Category.Digit
    elif letter == "*":
        letter_category = Category.Asterisk
    else:
        letter_category = Category.Other

    return letter_category


def main():
    with open("input", "r") as file:
        data = ["." + line.strip() + "." for line in file.readlines()]
        data = ["." * len(data[0])] + data + ["." * len(data[0])]

    gears = defaultdict(lambda: set())
    for row in range(1, len(data)-1):
        number = ""
        cur_gears = set()

        for column in range(1, len(data[0])-1):
            match categorize_letter(data[row][column]):
                case Category.Digit:
                    number += data[row][column]
                    for i, j in product(range(-1, 2), repeat=2):
                        if categorize_letter(data[row+i][column+j]) == Category.Asterisk:
                            cur_gears.add((row+i, column+j))
                case Category.Asterisk | Category.Other:
                    if number != "" and cur_gears:
                        for gear in cur_gears:
                            gears[gear].add(int(number))
                    number = ""
                    cur_gears = set()

        if number != "" and cur_gears:
            for gear in cur_gears:
                gears[gear].add(int(number))

    s = 0
    for numbers in gears.values():
        if len(numbers) == 2:
            s += reduce(lambda x, y: x*y, numbers)

    print(s)


if __name__ == "__main__":
    main()
