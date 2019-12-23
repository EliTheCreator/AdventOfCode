import collections
import queue
import re
import threading

shutdownRequestFlag = False


def intcode(mem, inputQ: queue.SimpleQueue, outputQ: queue.SimpleQueue):
    global shutdownRequestFlag
    i = 0
    relBase = 0
    inputPacketBuffer = queue.SimpleQueue()
    while not shutdownRequestFlag:
        instr = mem[i]
        op = instr % 100
        modeP1 = instr // 100 % 10
        modeP2 = instr // 1000 % 10
        modeP3 = instr // 10000 % 10

        # End-Of-Program
        if op == 99:
            print("Shutdown")
            break

        indexP1 = (relBase + mem[i+1] if modeP1 ==
                   2 else i + 1) if modeP1 else mem[i+1]

        if op == 3 or op == 4 or op == 9:
            # Input
            if op == 3:
                if not inputQ.empty():
                    packet = inputQ.get()
                    for packetPart in packet:
                        inputPacketBuffer.put(packetPart)

                if inputPacketBuffer.empty():
                    mem[indexP1] = -1
                else:
                    mem[indexP1] = inputPacketBuffer.get()
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

    NICs = []
    inputQs = []
    outputQs = []
    for address in range(50):
        inputQ = queue.SimpleQueue()
        inputQ.put(tuple([address]))
        inputQs.append(inputQ)
        outputQ = queue.SimpleQueue()
        outputQs.append(outputQ)
        NICs.append(threading.Thread(target=intcode, args=[
                    memory.copy(), inputQ, outputQ]))

    for NIC in NICs:
        NIC.start()

    while not shutdownRequestFlag:
        for outputQ in outputQs:
            if not outputQ.empty():
                address = outputQ.get()
                x = outputQ.get()
                y = outputQ.get()

                if address != 255:
                    inputQs[address].put((x, y))
                else:
                    print(y)
                    shutdownRequestFlag = True
                    break

    for NIC in NICs:
        NIC.join()


if __name__ == "__main__":
    main()
