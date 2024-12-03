import re


def main():
    with open("input", "r") as file:
        data = [re.findall(r"mul\((\d+),(\d+)\)", line) for line in file.readlines()]

    total = 0
    for line in data:
        for a, b in line:
            total += int(a)*int(b)

    print(total)


if __name__ == "__main__":
    main()
