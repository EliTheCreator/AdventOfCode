import collections
import queue
import re
import threading


def intcode(mem, inputQ: queue.SimpleQueue, outputQ: queue.SimpleQueue):
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
    file = open("input", "r")
    program = [int(x) for x in re.findall(r"-?\d+", file.readline())]
    memory = collections.defaultdict(lambda: 0, enumerate(program))
    file.close()

    inputQ = queue.SimpleQueue()
    outputQ = queue.SimpleQueue()
    arcade = threading.Thread(target=intcode, args=[memory, inputQ, outputQ])

    arcade.start()
    arcade.join()

    tiles = collections.defaultdict(lambda: 0)
    counter = 0
    while not outputQ.empty():
        x = outputQ.get()
        y = outputQ.get()
        tile = outputQ.get()

        if tile == 2:
            counter += 1

        tiles[(x, y)] = tile

    # minX = min(tiles.items(), key=lambda x: x[0][0])[0][0]
    # maxX = max(tiles.items(), key=lambda x: x[0][0])[0][0]
    # minY = min(tiles.items(), key=lambda x: x[0][1])[0][1]
    # maxY = max(tiles.items(), key=lambda x: x[0][1])[0][1]
    # print(minX, maxX, minY, maxY)

    # for j in range(minY, maxY + 1):
    #     for i in range(minX, maxX + 1):
    #         tile = tiles[(i, j)]
    #         if tile:
    #             print(tile, end="")
    #         else:
    #             print(" ", end="")
    #     print("")

    print(counter)


if __name__ == "__main__":
    main()
