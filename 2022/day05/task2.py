import re


def main():
    with open("input", "r") as file:
        stacksRaw, movesRaw = file.read().split("\n\n")

    stackLines = stacksRaw.split("\n")
    stackCount = int(stackLines[-1].split(" ")[-2].strip())

    stacks: dict[list[str]] = {}
    for stackNum in range(1, stackCount+1):
        stacks[stackNum] = []

    for line in reversed(stackLines[:-1]):
        for stackNum, pos in enumerate(range(1, len(line), 4), 1):
            if line[pos] != ' ':
                stacks[stackNum].append(line[pos])

    moves = [[int(x) for x in re.findall(r"\d+", line)] for line in movesRaw.split("\n")]

    for count, fromNum, toNum in moves:
        stacks[toNum].extend(stacks[fromNum][-count:])
        stacks[fromNum] = stacks[fromNum][:-count]

    print("".join([stacks[num][-1] for num in range(1, stackCount+1)]))


if __name__ == "__main__":
    main()
