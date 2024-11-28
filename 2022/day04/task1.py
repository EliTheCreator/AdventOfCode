import re


def main():
    with open("input", "r") as file:
        data = [[int(n) for n in re.findall(r"\d+", line)] for line in file.readlines()]

    result = 0
    for l1, l2, r1, r2 in data:
        if l1<=r1 and r2<=l2 or r1<=l1 and l2<=r2:
            result += 1

    print(result)


if __name__ == "__main__":
    main()
