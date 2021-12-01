import re


def main():
    with open("input", "r") as file:
        measurements = [int(x) for x in file.readlines()]

    print(len([True for (x, y) in zip(measurements[:-1], measurements[1:]) if x < y]))


if __name__ == "__main__":
    main()
