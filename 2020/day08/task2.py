import os
import re


def main():
    file = open("input", "r")
    memory = [[name, int(value)] for name, value in
              [re.findall(r"\w{3}|[+-]\d+", line)
               for line in file.readlines()]]
    file.close()

    def emulate():
        visited = set()
        accumulator = 0
        pc = 0
        while pc not in visited:
            if pc >= len(memory):
                return accumulator
            visited.add(pc)
            ins, num = memory[pc]
            if ins == "nop":
                pc += 1
            elif ins == "acc":
                accumulator += num
                pc += 1
            elif ins == "jmp":
                pc += num
        return None

    for pos, (ins, _) in enumerate(memory):
        result = None
        if ins == "jmp":
            memory[pos][0] = "nop"
            result = emulate()
            memory[pos][0] = "jmp"
        elif ins == "nop":
            memory[pos][0] = "jmp"
            result = emulate()
            memory[pos][0] = "nop"

        if result is not None:
            print(result)
            break


if __name__ == "__main__":
    main()
