import re


def main():
    with open("input", "r") as file:
        data = [[int(x) for x in re.findall(r"\d+", line)]
                for line in file.readlines()]

    print(sum((max(line) - min(line) for line in data)))


if __name__ == "__main__":
    main()
