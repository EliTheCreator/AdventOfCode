from collections import deque
from functools import reduce
import re


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


def lcm(a: int, b: int) -> int:
    return (a*b)//gcd(a, b)


def main():
    with open("example", "r") as file:
        monkeysRaw = [[line.strip() for line in monkey.split("\n")]
                      for monkey in file.read().split("\n\n")]

    monkeys = []
    divisors = []
    for monkey in monkeysRaw:
        items = [int(item) for item in re.findall(r"\d+", monkey[1])]
        operation = monkey[2].split(" ")[-3:]
        test = int(monkey[-3].split(" ")[-1])
        throwToTrue = int(monkey[-2].split(" ")[-1])
        throwToFalse = int(monkey[-1].split(" ")[-1])
        monkeys.append({
            "items": deque(items),
            "operation": operation,
            "test": test,
            "throwToTrue": throwToTrue,
            "throwToFalse": throwToFalse,
            "inspections": 0
        })
        divisors.append(test)

    divisor = reduce(lcm, divisors)

    for _ in range(10000):
        for monkey in monkeys:
            while monkey["items"]:
                item = monkey["items"].popleft()
                op1 = item if monkey["operation"][0] == "old" else int(monkey["operation"][0])
                op2 = item if monkey["operation"][2] == "old" else int(monkey["operation"][2])
                match monkey["operation"][1]:
                    case "+":
                        item = op1 + op2
                    case "*":
                        item = op1 * op2
                    case _:
                        pass

                item = item%divisor
                monkey["inspections"] += 1

                if item%monkey["test"] == 0:
                    monkeys[monkey["throwToTrue"]]["items"].append(item)
                else:
                    monkeys[monkey["throwToFalse"]]["items"].append(item)

    monkeys = sorted(monkeys, key=lambda monkey: monkey["inspections"])
    print(monkeys[-2]["inspections"] * monkeys[-1]["inspections"])


if __name__ == "__main__":
    main()
