from collections import defaultdict


def main():
    with open("input", "r") as file:
        instructions = [line.strip().split(" ") for line in file.readlines()]

    regNames = "abcd"
    regs = defaultdict(lambda: 0)
    pc = 0
    while True:
        instr = instructions[pc]
        pc += 1
        match instr:
            case "cpy", x, y:
                regs[y] = regs[x] if x in regNames else int(x)
            case "inc", x:
                regs[x] += 1
            case "dec", x:
                regs[x] -= 1
            case "jnz", x, y:
                cond = regs[x] if x in regNames else int(x)
                val = regs[y] if y in regNames else int(y)
                if cond:
                    pc += val - 1
            case _:
                print(f"Invalid instruction: {instr}")

        if pc >= len(instructions):
            break

    print(regs["a"])


if __name__ == "__main__":
    main()
