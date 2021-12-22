import re


def main():
    with open("input", "r") as file:
        jumps = [int(x) for x in re.findall(r"-?\d+", file.read())]

    pos = 0
    steps = 0
    while 0 <= pos and pos < len(jumps):
        jumpLength = jumps[pos]
        jumps[pos] += 1
        pos += jumpLength
        steps += 1

    print(steps)


if __name__ == "__main__":
    main()
