import re


def main():
    with open("input", "r") as file:
        data = [[int(n) for n in re.findall(r"\d+", line)] for line in file.readlines()]

    result = 0
    for l1, l2, r1, r2 in data:
        if not (l2<r1 or r2<l1):
            result += 1

    print(result)


if __name__ == "__main__":
    main()
