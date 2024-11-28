from enum import IntEnum
from itertools import product
from string import digits


class Category(IntEnum):
    Period = 0
    Symbol = 1
    Digit = 2


def categorize_letter(letter) -> Category:
    letter_category: Category
    if letter == ".":
        letter_category = Category.Period
    elif letter in digits:
        letter_category = Category.Digit
    else:
        letter_category = Category.Symbol

    return letter_category


def main():
    with open("input", "r") as file:
        data = ["." + line.strip() + "." for line in file.readlines()]
        data = ["." * len(data[0])] + data + ["." * len(data[0])]

    s = 0
    for row in range(1, len(data)-1):
        number = ""
        add_to_sum = False

        for column in range(1, len(data[0])-1):
            match categorize_letter(data[row][column]):
                case Category.Digit:
                    number += data[row][column]
                    for i, j in product(range(-1, 2), repeat=2):
                        if categorize_letter(data[row+i][column+j]) == Category.Symbol:
                            add_to_sum = True
                            break
                case Category.Symbol | Category.Period:
                    if number != "" and add_to_sum:
                        s += int(number)
                    number = ""
                    add_to_sum = False

        if number != "" and add_to_sum:
            s += int(number)

    print(s)


if __name__ == "__main__":
    main()
