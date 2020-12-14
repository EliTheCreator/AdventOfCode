import re


def parseLine(line):
    if line[:4] == "mask":
        raw_mask = line.strip().split(" = ")[1]
        premask = 0
        mask = 0
        for bit in range(35, -1, -1):
            if raw_mask[35 - bit] == 'X':
                premask ^= 1 << bit
            elif raw_mask[35 - bit] == '1':
                mask |= 1 << bit
        return (0, (premask, mask))
    elif line[:3] == "mem":
        return (1, tuple([int(x) for x in re.findall(r"\d+", line)]))


def main():
    file = open("input", "r")
    instructions = [parseLine(line) for line in file.readlines()]
    file.close()

    premask = 0
    mask = 0
    memory = {}
    for instr, (oprnd1, oprnd2) in instructions:
        if instr == 0:
            premask = oprnd1
            mask = oprnd2
        elif instr == 1:
            memory[oprnd1] = (oprnd2 & premask) ^ mask

    s = 0
    for key in memory.keys():
        s += memory[key]

    print(s)


if __name__ == "__main__":
    main()
