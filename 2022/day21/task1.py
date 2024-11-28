from collections import deque


class Monkey():
    value: int
    left: str
    right: str
    op: str

    def __init__(self, value, left, op, right):
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
        if len(other) == 1:
            monkey = Monkey(int(other[0]), None, None, None)
        else:
            monkey = Monkey(None, *other)
        monkeys[name] = monkey

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
            leftVal = monkeys[monkey.left].value
            rightVal = monkeys[monkey.right].value
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

    print(monkeys["root"].value)


if __name__ == "__main__":
    main()
