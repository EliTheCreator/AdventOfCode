import itertools
import queue
import re
import threading


def computer(program, inputQ: queue.SimpleQueue, outputQ: queue.SimpleQueue):
    i = 0

    while i < len(program):
        instr = program[i]
        op = instr % 100
        modeP1 = instr // 100 % 10
        modeP2 = instr // 1000 % 10
        modeP3 = instr // 10000 % 10

        # Add or Multiplie
        if op == 1 or op == 2:
            p1 = program[i+1] if modeP1 else program[program[i+1]]
            p2 = program[i+2] if modeP2 else program[program[i+2]]
            result = p1 + p2 if op == 1 else p1 * p2
            if modeP3:
                program[i+3] = result
            else:
                program[program[i+3]] = result
            i += 4
        # Input
        elif op == 3:
            inp = inputQ.get()

            if modeP1:
                program[i+1] = inp
            else:
                program[program[i+1]] = inp
            i += 2
        # Output
        elif op == 4:
            outp = program[i+1] if modeP1 else program[program[i+1]]
            outputQ.put(outp)
            i += 2
        # Jump-If-True
        elif op == 5:
            p1 = program[i+1] if modeP1 else program[program[i+1]]
            p2 = program[i+2] if modeP2 else program[program[i+2]]
            if p1:
                i = p2
            else:
                i += 3
        # Jump-If-False
        elif op == 6:
            p1 = program[i+1] if modeP1 else program[program[i+1]]
            p2 = program[i+2] if modeP2 else program[program[i+2]]
            if p1:
                i += 3
            else:
                i = p2
        # Less-Than
        elif op == 7:
            p1 = program[i+1] if modeP1 else program[program[i+1]]
            p2 = program[i+2] if modeP2 else program[program[i+2]]
            result = 1 if p1 < p2 else 0
            if modeP3:
                program[i+3] = result
            else:
                program[program[i+3]] = result
            i += 4
        # Equals
        elif op == 8:
            p1 = program[i+1] if modeP1 else program[program[i+1]]
            p2 = program[i+2] if modeP2 else program[program[i+2]]
            result = 1 if p1 == p2 else 0
            if modeP3:
                program[i+3] = result
            else:
                program[program[i+3]] = result
            i += 4
        # End-Of-Program
        elif op == 99:
            break
        # Illegal Instruction
        else:
            print("Error: unknown Instruction")
            print(
                f"Instr:{str(instr).zfill(5)} Op:{op} P1:{modeP1} P2:{modeP2} P3:{modeP3}")
            return


def main():
    file = open("input", "r")
    program = [int(x) for x in re.findall("-?[0-9]+", file.readline())]
    file.close()

    maxSignal = 0

    for permutation in list(itertools.permutations([x for x in range(5, 10)])):
        atob = queue.SimpleQueue()
        atob.put(permutation[1])

        btoc = queue.SimpleQueue()
        btoc.put(permutation[2])

        ctod = queue.SimpleQueue()
        ctod.put(permutation[3])

        dtoe = queue.SimpleQueue()
        dtoe.put(permutation[4])

        etoa = queue.SimpleQueue()
        etoa.put(permutation[0])
        etoa.put(0)

        A = threading.Thread(target=computer, args=(
            program.copy(), etoa, atob))
        B = threading.Thread(target=computer, args=(
            program.copy(), atob, btoc))
        C = threading.Thread(target=computer, args=(
            program.copy(), btoc, ctod))
        D = threading.Thread(target=computer, args=(
            program.copy(), ctod, dtoe))
        E = threading.Thread(target=computer, args=(
            program.copy(), dtoe, etoa))

        threads = [A, B, C, D, E]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        signal = etoa.get()
        if maxSignal < signal:
            maxSignal = signal

    print(maxSignal)


main()
