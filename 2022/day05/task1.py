import re


def main():
    with open("input", "r") as file:
        stacks_raw, moves_raw = file.read().split("\n\n")

    stack_lines = stacks_raw.split("\n")
    stack_count = int(stack_lines[-1].split(" ")[-2].strip())

    stacks: dict[list[str]] = {}
    for stack_num in range(1, stack_count+1):
        stacks[stack_num] = []

    for line in reversed(stack_lines[:-1]):
        for stack_num, pos in enumerate(range(1, len(line), 4), 1):
            if line[pos] != ' ':
                stacks[stack_num].append(line[pos])

    moves = [[int(x) for x in re.findall(r"\d+", line)] for line in moves_raw.split("\n")]

    for count, from_num, to_num in moves:
        for _ in range(count):
            stacks[to_num].append(stacks[from_num].pop())

    print("".join([stacks[num][-1] for num in range(1, stack_count+1)]))


if __name__ == "__main__":
    main()
