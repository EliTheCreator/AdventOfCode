import re


def main():
    with open("input", "r") as file:
        data = [
            re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", line)
            for line in file.readlines()
        ]

    total = 0
    enabled = True
    for line in data:
        for a, b, do, dont in line:
            if do:
                enabled = True
            elif dont:
                enabled = False
            else:
                if not enabled:
                    continue
                total += int(a)*int(b)

    print(total)


if __name__ == "__main__":
    main()
