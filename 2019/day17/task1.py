import collections
import queue
import re
import threading

shutdownRequestFlag = False


def intcode(mem, inputQ: queue.SimpleQueue, outputQ: queue.SimpleQueue):
    global shutdownRequestFlag
    i = 0
    relBase = 0
    while not shutdownRequestFlag:
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
                mem[indexP1] = inputQ.get()
            # Output
            elif op == 4:
                outputQ.put(mem[indexP1])
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


def main():
    global shutdownRequestFlag

    file = open("input", "r")
    program = [int(x) for x in re.findall(r"-?\d+", file.readline())]
    memory = collections.defaultdict(lambda: 0, enumerate(program))
    file.close()

    inputQ = queue.SimpleQueue()
    outputQ = queue.SimpleQueue()
    computer = threading.Thread(target=intcode, args=[memory, inputQ, outputQ])

    computer.start()
    computer.join()

    screenRaw = []
    while not outputQ.empty():
        screenRaw.append(chr(outputQ.get()))

    screen = [s for s in "".join(screenRaw).split("\n")][:-2]
    # screen2 = [["." for _ in range(len(screen[0] + 2)) for _ in range(len(screen) + 2)]]
    # for j, row in enumerate(screen):
    #     for i, s in enumerate(row):
    #         screen2[j][i] = s

    # screen = "".join(screenRaw)

    # print(screen)
    # for s in screen:
    #     print(s)
    # print(len(screen))
    # print(len(screen[0]))

    sumOfAlignmentParams = 0
    for j in range(1, len(screen) - 1):
        for i in range(1, len(screen[0]) - 1):
            # print(j, i)
            if screen[j][i] == "#":
                if screen[j-1][i] == "#":
                    if screen[j][i-1] == "#":
                        if screen[j][i+1] == "#":
                            if screen[j+1][i] == "#":
                                sumOfAlignmentParams += i * j

    print(sumOfAlignmentParams)


if __name__ == "__main__":
    main()
