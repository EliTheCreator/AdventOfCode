import collections
import os
import queue
import re
import threading

flag = False


def intcode(mem, inputQ: queue.SimpleQueue, outputQ: queue.SimpleQueue):
    global flag
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
                flag = True
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
    global flag
    file = open("input", "r")
    program = [int(x) for x in re.findall(r"-?\d+", file.readline())]
    program[0] = 2
    memory = collections.defaultdict(lambda: 0, enumerate(program))
    file.close()

    inputQ = queue.SimpleQueue()
    outputQ = queue.SimpleQueue()
    arcade = threading.Thread(target=intcode, args=[memory, inputQ, outputQ])
    arcade.start()

    tiles = collections.defaultdict(lambda: 0)
    score = 0
    counter = 0
    while arcade.is_alive() or not outputQ.empty():
        if flag or not arcade.is_alive():
            flag = False
            while not outputQ.empty():
                x = outputQ.get()
                y = outputQ.get()
                tile = outputQ.get()
                if x != -1:
                    tiles[(x, y)] = tile
                else:
                    counter += 1
                    score = tile
                    # print(f"{counter}: {score}")

            if counter > -1:
                os.system("cls")
                for j in range(23):
                    for i in range(45):
                        tile = tiles[(i, j)]
                        if tile:
                            print(tile, end="")
                        else:
                            print(" ", end="")
                    print("")

            # inp = input().strip()
            # if inp == "a":
            #     inputQ.put(-1)
            # elif inp == "d":
            #     inputQ.put(1)
            # else:
            #     inputQ.put(0)

            xBall = 0
            xPaddle = 0
            for (x, y), value in tiles.items():
                if value == 3:
                    xPaddle = x
                elif value == 4:
                    xBall = x

            inputQ.put(xBall - xPaddle)

    arcade.join()

    print(score)


if __name__ == "__main__":
    main()
