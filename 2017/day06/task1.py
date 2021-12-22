import re


def main():
    with open("input", "r") as file:
        banks = [int(x) for x in re.findall(r"\d+", file.readline())]

    cycles = 0
    configurations = set()
    while True:
        config = tuple(banks)
        if config in configurations:
            print(cycles)
            return

        configurations.add(config)
        cycles += 1

        i, val = max(enumerate(banks), key=lambda x: x[1])

        banks[i] = 0
        j = i
        for _ in range(val):
            j = (j + 1) % len(banks)
            banks[j] += 1


if __name__ == "__main__":
    main()
