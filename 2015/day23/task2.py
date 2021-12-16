from collections import defaultdict


def main():
    with open("input", "r") as file:
        program = [line.strip().split(" ") for line in file.readlines()]

    regNames = "ab"
    regs = defaultdict(lambda: 0, [("a", 1)])
    pc = 0
    while pc < len(program):
        instr = program[pc]
        pc += 1
        match instr:
            case "hlf", r:
                regs[r] //= 2
            case "tpl", r:
                regs[r] *= 3
            case "inc", r:
                regs[r] += 1
            case "jmp", r:
                pc -= 1
                pc += regs[r] if r in regNames else int(r)
            case "jie", r, o:
                if regs[r[:-1]] % 2 == 0:
                    pc -= 1
                    pc += int(o)
            case "jio", r, o:
                if regs[r[:-1]] == 1:
                    pc -= 1
                    pc += int(o)

    print(regs["b"])


if __name__ == "__main__":
    main()
