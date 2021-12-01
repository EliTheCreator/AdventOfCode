import re


def main():
    file = open("sample", "r")
    lines = [line.strip() for line in file.readlines()]
    file.close()

    length = 0
    for line in lines:
        xs = len(re.findall(r"\\x", line))
        l = len(line)
        length += l + (l - len(eval(line))) + 4 + 2 * xs

    print(length)


if __name__ == "__main__":
    main()
