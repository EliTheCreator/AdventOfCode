import re


def parseLine(line):
    if line[:4] == "mask":
        raw_mask = line.strip().split(" = ")[1]
        masks = set([(0, 0)])
        for bit in raw_mask:
            new_masks = set()
            for premask, mask in masks:
                premask = premask << 1
                mask = mask << 1
                if bit == 'X':
                    new_masks.add((premask, mask | 1))
                    new_masks.add((premask, mask | 0))
                elif bit == '1':
                    new_masks.add((premask | 1, mask | 1))
                elif bit == '0':
                    new_masks.add((premask | 1, mask | 0))

            masks = new_masks
        return (0, masks)
    elif line[:3] == "mem":
        return (1, tuple([int(x) for x in re.findall(r"\d+", line)]))


def main():
    file = open("input", "r")
    instructions = [parseLine(line) for line in file.readlines()]
    file.close()
    print("parsed file")
    masks = set()
    memory = {}
    for instr, oprnds in instructions:
        if instr == 0:
            masks = oprnds
        elif instr == 1:
            for premask, mask in masks:
                memory[(oprnds[0] & premask) | mask] = oprnds[1]

    s = 0
    for key in memory.keys():
        s += memory[key]

    print(s)


if __name__ == "__main__":
    main()
