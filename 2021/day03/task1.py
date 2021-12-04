import functools
import re


def main():
    with open("input", "r") as file:
        data = [[int(x) for x in re.findall("[01]", line)]
                for line in file.readlines()]

    columns = len(data)

    sums = functools.reduce(lambda x, y: [a + b for (a, b) in zip(x, y)], data)

    gamma = int("".join(["1" if x > (columns/2) else "0" for x in sums]), 2)
    epsilon = int("".join(["1" if x <= (columns/2) else "0" for x in sums]), 2)

    print(gamma * epsilon)


if __name__ == "__main__":
    main()
