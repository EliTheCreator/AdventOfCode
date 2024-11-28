from collections import deque


class Monkey():
    fromHuman: bool
    value: str
    left: str
    right: str
    op: str

    def __init__(self, fromHuman, value, left, op, right):
        self.fromHuman = fromHuman
        self.value = value
        self.left = left
        self.op = op
        self.right = right


def main():
    with open("input", "r") as file:
        data = [line.strip().split(": ") for line in file.readlines()]

    monkeys: dict[str, Monkey] = {}
    for name, other in data:
        other = other.split(" ")
        fromHuman = name == "humn"
        if len(other) == 1:
            monkey = Monkey(fromHuman, int(other[0]), None, None, None)
        else:
            monkey = Monkey(fromHuman, None, *other)
        monkeys[name] = monkey

    monkeys["root"].op = "=="

    stack = []
    queue = deque()
    queue.append("root")
    while queue:
        name = queue.popleft()
        stack.append(name)
        monkey = monkeys[name]

        if monkey.left:
            queue.append(monkey.left)
        if monkey.right:
            queue.append(monkey.right)

    for name in reversed(stack):
        monkey = monkeys[name]
        if not monkey.value:
            left = monkeys[monkey.left]
            right = monkeys[monkey.right]
            if not left.fromHuman and not right.fromHuman:
                leftVal = left.value
                rightVal = right.value
                match monkey.op:
                    case "-":
                        monkey.value = leftVal - rightVal
                    case "+":
                        monkey.value = leftVal + rightVal
                    case "*":
                        monkey.value = leftVal * rightVal
                    case "/":
                        monkey.value = leftVal // rightVal
                    case _:
                        pass
            else:
                monkey.fromHuman = True

    value: int
    name = "root"
    while name != "humn":
        monkey = monkeys[name]
        left = monkeys[monkey.left]
        right = monkeys[monkey.right]
        leftVal = left.value
        rightVal = right.value
        if left.fromHuman:
            match monkey.op:
                case "-":
                    value += rightVal
                case "+":
                    value -= rightVal
                case "*":
                    value //= rightVal
                case "/":
                    value *= rightVal
                case _:
                    value = right.value
            name = monkey.left
        else:
            match monkey.op:
                case "-":
                    value = leftVal - value
                case "+":
                    value -= leftVal
                case "*":
                    value //= leftVal
                case "/":
                    value = leftVal // value
                case _:
                    value = left.value
            name = monkey.right

    print(value)


if __name__ == "__main__":
    main()
