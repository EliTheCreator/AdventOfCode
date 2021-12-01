import re


def main():
    with open("input", "r") as file:
        mes = [int(x) for x in file.readlines()]

    sums = [x + y + z for ((x, y), z)
            in zip(zip(mes[2:], mes[1:-1]), mes[:-2])]

    print(len([True for (x, y) in zip(sums[:-1], sums[1:]) if x < y]))


if __name__ == "__main__":
    main()
