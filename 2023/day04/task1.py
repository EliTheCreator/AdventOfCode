import re


def main():
    with open("input", "r") as file:
        data = [[int(x) for x in re.findall(r"\d+", line)] for line in file.readlines()]

    s = 0
    for line in data:
        s += int(2**(len(set.intersection(set(line[1:11]), set(line[11:])))-1))

    print(s)


if __name__ == "__main__":
    main()
