import re


def main():
    file = open("input", "r")
    ip_reg = int(re.findall(r"\d", file.readline())[0])
    program = [(lambda l: (l[0], [int(x) for x in re.findall(r"\d+", l[1])]))
               (line.split(" ", maxsplit=1)) for line in file.readlines()]
    file.close()

    instructions = {
        "addr": lambda r, i: r[i[0]] + r[i[1]],
        "addi": lambda r, i: r[i[0]] + i[1],
        "mulr": lambda r, i: r[i[0]] * r[i[1]],
        "muli": lambda r, i: r[i[0]] * i[1],
        "banr": lambda r, i: r[i[0]] & r[i[1]],
        "bani": lambda r, i: r[i[0]] & i[1],
        "borr": lambda r, i: r[i[0]] | r[i[1]],
        "bori": lambda r, i: r[i[0]] | i[1],
        "setr": lambda r, i: r[i[0]],
        "seti": lambda r, i: i[0],
        "gtir": lambda r, i: 1 if i[0] > r[i[1]] else 0,
        "gtri": lambda r, i: 1 if r[i[0]] > i[1] else 0,
        "gtrr": lambda r, i: 1 if r[i[0]] > r[i[1]] else 0,
        "eqir": lambda r, i: 1 if i[0] == r[i[1]] else 0,
        "eqri": lambda r, i: 1 if r[i[0]] == i[1] else 0,
        "eqrr": lambda r, i: 1 if r[i[0]] == r[i[1]] else 0,
    }

    ip = 0
    registers = [0 for _ in range(6)]
    while 0 <= ip < len(program):
        opcode, oprnds = program[ip]
        registers[oprnds[2]] = (instructions[opcode])(registers, oprnds)
        registers[ip_reg] += 1
        ip = registers[ip_reg]

    print(registers[0])


if __name__ == "__main__":
    main()
