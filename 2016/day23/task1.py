from collections import defaultdict


def main():
    with open("input", "r") as file:
        program = [line.strip().split(" ") for line in file.readlines()]

    regNames = "abcd"
    regs = defaultdict(lambda: 0, {"a": 7})
    pc = 0
    while True:
        instr = program[pc]
        pc += 1
        match instr:
            case "cpy", x, y:
                if y in regNames:
                    regs[y] = regs[x] if x in regNames else int(x)
            case "inc", x:
                if x in regNames:
                    regs[x] += 1
            case "dec", x:
                if x in regNames:
                    regs[x] -= 1
            case "jnz", x, y:
                cond = regs[x] if x in regNames else int(x)
                val = regs[y] if y in regNames else int(y)
                if cond:
                    pc += val - 1
            case "tgl", x:
                line = regs[x] if x in regNames else int(x)
                line += pc - 1
                if 0 <= line and line < len(program):
                    match program[line]:
                        case "inc", *_:
                            program[line][0] = "dec"
                        case "dec", *_:
                            program[line][0] = "inc"
                        case "tgl", *_:
                            program[line][0] = "inc"
                        case "jnz", *_:
                            program[line][0] = "cpy"
                        case "cpy", *_:
                            program[line][0] = "jnz"
            case _:
                print(f"Invalid instruction: {instr}")

        if pc >= len(program):
            break

    print(regs["a"])


if __name__ == "__main__":
    main()
