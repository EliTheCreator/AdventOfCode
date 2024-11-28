import re


def replace_spelled_out(elem):
    match elem:
        case "one":
            new_elem = "1"
        case "two":
            new_elem = "2"
        case "three":
            new_elem = "3"
        case "four":
            new_elem = "4"
        case "five":
            new_elem = "5"
        case "six":
            new_elem = "6"
        case "seven":
            new_elem = "7"
        case "eight":
            new_elem = "8"
        case "nine":
            new_elem = "9"
        case _:
            new_elem = elem

    return new_elem


def main():
    pattern = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")
    with open("input", "r") as file:
        data = [[match.group(1) for match in pattern.finditer(line)] for line in file.readlines()]

    data = [[replace_spelled_out(elem) for elem in line] for line in data]

    print(sum(int(line[0] + line[-1]) for line in data))


if __name__ == "__main__":
    main()
