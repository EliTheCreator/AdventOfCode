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

    currentWalkingDirection = 0
    walkingDirections = (1, 4, 2, 3)
    x = 0
    y = 0
    ship = collections.defaultdict(lambda: 0)
    ship[(x, y)] = 1
    startingPosition = (0, 0)

    # 0 : hit wall
    # 1 : moved in direction
    # 2 : has moved and found oxygen system

    # 1 : up
    # 2 : down
    # 3 : left
    # 4 : right

    inputQ = queue.SimpleQueue()
    outputQ = queue.SimpleQueue()
    droid = threading.Thread(target=intcode, args=[memory, inputQ, outputQ])

    droid.start()

    inputQ.put(1)
    droidReply = outputQ.get()
    while droidReply:
        y -= 1
        ship[(x, y)] = droidReply

    ship[(x, y-1)] = droidReply
    startingPosition = (x, y)
    currentWalkingDirection = currentWalkingDirection + 1

    while True:
        nextWalkingDirection = (currentWalkingDirection - 1) % 4
        nextX = x
        nextY = y
        for _ in range(4):
            inputQ.put(walkingDirections[nextWalkingDirection])

            if nextWalkingDirection == 0:
                nextY -= 1
            elif nextWalkingDirection == 1:
                nextX += 1
            elif nextWalkingDirection == 2:
                nextY += 1
            elif nextWalkingDirection == 3:
                nextX -= 1

            droidReply = outputQ.get()
            ship[(nextX, nextY)] = droidReply

            if droidReply:
                currentWalkingDirection = nextWalkingDirection
                x = nextX
                y = nextY
                break
            else:
                nextX = x
                nextY = y
                nextWalkingDirection = (nextWalkingDirection + 1) % 4

        if (x, y) == startingPosition:
            break

    shutdownRequestFlag = True
    inputQ.put(0)
    droid.join()

    print("Print Labyrinth?")
    if int(input()):
        minX = min(ship.items(), key=lambda x: x[0][0])[0][0]
        maxX = max(ship.items(), key=lambda x: x[0][0])[0][0]
        minY = min(ship.items(), key=lambda x: x[0][1])[0][1]
        maxY = max(ship.items(), key=lambda x: x[0][1])[0][1]

        for j in range(minY, maxY + 1):
            for i in range(minX, maxX + 1):
                if ship[(i, j)]:
                    if ship[(i, j)] == 1:
                        print(" ", end='')
                    else:
                        print("O", end='')
                else:
                    print("#", end='')
            print("")

    commands = 0
    visited = set()
    toVisit = set([(0, 0)])

    while toVisit:
        nextLevel = set()
        for (x, y) in toVisit:
            visited.add((x, y))

            up = (x, y-1)
            upVal = ship[up]
            if upVal and up not in visited:
                nextLevel.add(up)

            right = (x+1, y)
            rightVal = ship[right]
            if rightVal and right not in visited:
                nextLevel.add(right)

            down = (x, y+1)
            downVal = ship[down]
            if downVal and down not in visited:
                nextLevel.add(down)

            left = (x-1, y)
            leftVal = ship[left]
            if leftVal and left not in visited:
                nextLevel.add(left)

            if 2 in [upVal, downVal, leftVal, rightVal]:
                nextLevel = set()
                break

        toVisit = nextLevel
        commands += 1

    print(commands)


if __name__ == "__main__":
    main()
