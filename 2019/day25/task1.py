import collections
import itertools
import queue
import re
import threading

shutdownRequestFlag = False
printerShutdownFlag = False


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


def droidOutputPrinter(outputQ: queue.SimpleQueue):
    global printerShutdownFlag

    while not printerShutdownFlag:
        while not outputQ.empty():
            print(chr(outputQ.get()), end="")


def main():
    global shutdownRequestFlag
    global printerShutdownFlag

    file = open(".\\input", "r")
    program = [int(x) for x in re.findall(r"-?\d+", file.readline())]
    memory = collections.defaultdict(lambda: 0, enumerate(program))
    file.close()

    inputQ = queue.SimpleQueue()
    outputQ = queue.SimpleQueue()

    droid = threading.Thread(target=intcode, args=[memory, inputQ, outputQ])
    printer = threading.Thread(target=droidOutputPrinter, args=[outputQ])

    droid.start()
    printer.start()

    # items needed => 'mutex', 'cake', 'fuel cell', 'coin'
    while not shutdownRequestFlag:
        droidCommand = input()
        if droidCommand == "automate":
            printerShutdownFlag = True
            break
        if droidCommand == "exit":
            shutdownRequestFlag = True
            printerShutdownFlag = True
        for c in droidCommand:
            inputQ.put(ord(c))
        inputQ.put(ord("\n"))

    # for c in "inv\n":
    #     inputQ.put(ord(c))

    # answer = []
    # while outputQ[0] != ord("?"):
    #     answer.append(ord(outputQ.get()))
    # answer = "".join(answer)

    # commands = open("commands", "r")
    # for line in commands:
    #     for c in line:
    #         inputQ.put(ord(c))

    # while not outputQ.empty():
    #     print(chr(outputQ.get(timeout=2)), end="")

    # items = ["dehydrated water", "candy cane", "manifold",
    #          "mutex", "cake", "prime number", "fuel cell", "coin"]
    # found = False
    # for count in range(1, len(items) + 1):
    #     if found:
    #         break
    #     for perm in itertools.combinations(items, count):
    #         print(perm)
    #         for item in perm:
    #             for c in f"take {item}\n":
    #                 inputQ.put(ord(c))

    #         for c in "west\n":
    #             inputQ.put(ord(c))

    #         while not outputQ.empty():
    #             print(chr(outputQ.get(timeout=2)), end="")

    #         if input() == "y":
    #             found = True
    #             printerShutdownFlag = False
    #             break

    #         for item in perm:
    #             for c in f"drop {item}\n":
    #                 inputQ.put(ord(c))

    printer.join()

    # printer2 = threading.Thread(target=printDroidOutput, args=[outputQ])
    # printer2.start()
    # while not shutdownRequestFlag:
    #     droidCommand = input()
    #     if droidCommand == "exit":
    #         shutdownRequestFlag = True
    #         printerShutdownFlag = True
    #     for c in droidCommand:
    #         inputQ.put(ord(c))
    #     inputQ.put(ord("\n"))

    droid.join()
    # printer2.join()


if __name__ == "__main__":
    main()
