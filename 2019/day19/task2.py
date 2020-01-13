import collections
import re


def intcode(mem, inputQ: collections.deque, outputQ: collections.deque):
    i = 0
    relBase = 0
    while True:
        instr = mem[i]
        op = instr % 100
        modeP1 = instr // 100 % 10
        modeP2 = instr // 1000 % 10
        modeP3 = instr // 10000 % 10

        # End-Of-Program
        if op == 99:
            break

        indexP1 = (relBase + mem[i+1] if modeP1 ==
                   2 else i + 1) if modeP1 else mem[i+1]

        if op == 3 or op == 4 or op == 9:
            # Input
            if op == 3:
                mem[indexP1] = inputQ.popleft()
            # Output
            elif op == 4:
                outputQ.append(mem[indexP1])
            # Adjust the relative Base
            elif op == 9:
                relBase += mem[indexP1]

            i += 2
        else:
            indexP2 = (relBase + mem[i+2] if modeP2 ==
                       2 else i + 2) if modeP2 else mem[i+2]
            if op == 5 or op == 6:
                # Jump-If-True
                if op == 5:
                    if mem[indexP1]:
                        i = mem[indexP2]
                    else:
                        i += 3
                # Jump-If-False
                elif op == 6:
                    if mem[indexP1]:
                        i += 3
                    else:
                        i = mem[indexP2]
            else:
                indexP3 = (relBase + mem[i+3] if modeP3 ==
                           2 else i + 3) if modeP3 else mem[i+3]
                # Add
                if op == 1:
                    mem[indexP3] = mem[indexP1] + mem[indexP2]
                # Multiplie
                elif op == 2:
                    mem[indexP3] = mem[indexP1] * mem[indexP2]
                # Less-Than
                elif op == 7:
                    mem[indexP3] = 1 if mem[indexP1] < mem[indexP2] else 0
                # Equals
                elif op == 8:
                    mem[indexP3] = 1 if mem[indexP1] == mem[indexP2] else 0
                # Illegal Instruction
                else:
                    print(f"Error: unknown Instruction")
                    print(
                        f"Instr:{str(instr).zfill(5)} Op:{op} P1:{modeP1} P2:{modeP2} P3:{modeP3}")
                    return

                i += 4


def isAffected(memory: collections.defaultdict, inputQ: collections.deque, outputQ: collections.deque, x: int, y: int):
    inputQ.append(x)
    inputQ.append(y)

    intcode(memory, inputQ, outputQ)

    memory[132] = 303
    memory[221] = 0
    memory[222] = 0
    memory[223] = 0
    memory[224] = 0
    memory[249] = 225

    return outputQ.popleft()


def main():
    file = open("input", "r")
    program = [int(x) for x in re.findall(r"-?\d+", file.readline())]
    memory = collections.defaultdict(lambda: 0, enumerate(program))
    file.close()

    inputQ = collections.deque()
    outputQ = collections.deque()

    # for y in range(50):
    #     for x in range(50):
    #         inputQ.append(x)
    #         inputQ.append(y)

    #         intcode(memory, inputQ, outputQ)

    #         memory[132] = 303
    #         memory[221] = 0
    #         memory[222] = 0
    #         memory[223] = 0
    #         memory[224] = 0
    #         memory[249] = 225

    #         answer = outputQ.popleft()
    #         print(answer, end="")
    #     print("")

    # startAtY = 100
    # y = 100
    # startAtX = 0
    # x = 0
    # while True:
    #     while True:
    #         answer = isAffected(memory, inputQ, outputQ, startAtX, startAtY)

    #         if answer == 0:
    #             startAtX += 1
    #         else:
    #             break

    #     x = startAtX
    #     count = 0
    #     while True:
    #         answer = isAffected(memory, inputQ, outputQ, x, startAtY)

    #         if answer == 1:
    #             x += 1
    #             count += 1
    #         else:
    #             break

    #     if count == 100:
    #         startAtY += 1
    #         continue
    #     else:
    #         y = startAtY


if __name__ == "__main__":
    main()
