import os
import re


def main():
    file = open("input", "r")
    memory = [(name, int(value)) for name, value in
              [re.findall(r"\w{3}|[+-]\d+", line)
               for line in file.readlines()]]
    file.close()

    visited = set()
    accumulator = 0
    pc = 0
    while pc not in visited:
        visited.add(pc)
        ins, num = memory[pc]
        if ins == "nop":
            pc += 1
        elif ins == "acc":
            accumulator += num
            pc += 1
        elif ins == "jmp":
            pc += num

    print(accumulator)


if __name__ == "__main__":
    main()
