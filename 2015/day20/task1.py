from itertools import count
from math import sqrt


def main():
    with open("input", "r") as file:
        minPresents = int(file.readline()) // 10

    def calcPresents(house):
        presents = 0
        for elve in range(1, int(sqrt(house)) + 1):
            if house % elve == 0:
                presents += elve
                presents += house // elve
        return presents

    for house in range(minPresents//6, minPresents // 2):
        if calcPresents(house) > minPresents:
            print(house)
            break


if __name__ == "__main__":
    main()
