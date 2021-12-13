import re


def main():
    with open("input", "r") as file:
        data = file.readlines()

    # regex1 = r"^(\w*|.*\])\w*(\w)(?:(?!\2)(\w))\3\2(?!.*\[\w*(\w)(?:(?!\4)(\w))\5\4\w*\])"
    regex1 = r"(\w)(?:(?!\1)(\w))\2\1"
    regex2 = r"\[\w*(\w)(?:(?!\1)(\w))\2\1\w*\]"
    filter1 = [True if re.search(regex1, line) else False for line in data]
    filter2 = [True if re.search(regex2, line) else False for line in data]
    print(sum((a and not b for a, b in zip(filter1, filter2))))


if __name__ == "__main__":
    main()
