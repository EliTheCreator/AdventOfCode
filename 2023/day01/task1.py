import re


def main():
    with open("input", "r") as file:
        data = [re.findall(r"\d", line) for line in file.readlines()]

    print(sum(int(line[0] + line[-1]) for line in data))


if __name__ == "__main__":
    main()
