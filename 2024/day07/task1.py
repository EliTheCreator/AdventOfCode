import re


def rec(goal: int, intermediate: int, operands: list[int]) -> int:
    match operands:
        case [x]:
            return (intermediate*x == goal) or intermediate+x == goal
        case [x, *xs]:
            if intermediate >= goal:
                return False
            else:
                return rec(goal, intermediate*x, xs) or rec(goal, intermediate+x, xs)


def main():
    with open("input", "r") as file:
        data = [[int(x) for x in re.findall(r"\d+", line)] for line in file.readlines()]

    total = 0
    for goal, operand, *operands in data:
        total += goal if rec(goal, operand, operands) else 0

    print(total)


if __name__ == "__main__":
    main()
