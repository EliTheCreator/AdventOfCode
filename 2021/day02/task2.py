import re


def main():
    with open("input", "r") as file:
        data = [(lambda s: (s[0], int(s[1])))(instr.split())
                for instr in re.findall("[a-z]+ [0-9]+", file.read())]

    horizontal_pos = 0
    depth = 0
    aim = 0

    for (direction, distance) in data:
        if direction == "forward":
            horizontal_pos += distance
            depth += aim * distance
        elif direction == "up":
            aim -= distance
        elif direction == "down":
            aim += distance
        else:
            print("Unknown direction encountered")

    print(horizontal_pos * depth)


if __name__ == "__main__":
    main()
