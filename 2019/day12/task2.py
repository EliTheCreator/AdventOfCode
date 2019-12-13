import itertools
import math
import re


def main():
    file = open("input", "r")
    positions = [[int(x) for x in re.findall("-?[0-9]+", line)]
                 for line in file]
    initPositions = list(
        zip(positions[0], positions[1], positions[2], positions[3]))
    print(initPositions)

    velocities = [[0, 0, 0] for _ in range(len(positions))]
    file.close()

    combinations = list(itertools.combinations(range(len(positions)), 2))

    for step in range(600000):
        # for moon, vel in enumerate(velocities):
        #     if not sum(map(abs, vel)):
        #         print(f"{moon}\tStep: {step}\t{positions[moon]}")

        # Calculate Velocity Vectors
        for first, second in combinations:
            firstPos = positions[first]
            firstVel = velocities[first]
            secondPos = positions[second]
            secondVel = velocities[second]

            for i in range(len(firstPos)):
                if firstPos[i] < secondPos[i]:
                    firstVel[i] += 1
                    secondVel[i] -= 1
                elif firstPos[i] > secondPos[i]:
                    firstVel[i] -= 1
                    secondVel[i] += 1

        # Calculate Position Vectors
        for i, (pos, vel) in enumerate(zip(positions, velocities)):
            positions[i] = [sum(p) for p in zip(pos, vel)]

        for i in range(len(initPositions)):
            axisVector = tuple([pos[i] for pos in positions])
            # print(axisVector)
            if initPositions[i] == axisVector:
                print(i, step)

    # totalEnergy = sum(sum(map(abs, pos)) * sum(map(abs, vel))
    #                   for pos, vel in zip(positions, velocities))

    # print(totalEnergy)


def lcm(a, b):
    return a*b // math.gcd(a, b)


def task2():
    # x axis
    # 572663 - 286331 = 286332

    # y axis
    # 386103 - 193051 = 193052

    # z axis
    # 204711 - 102355 = 102356
    x = 286332
    y = 193052
    z = 102356

    lcmxy = lcm(x, y)
    lcmxyz = lcm(lcmxy, z)
    print(lcmxyz)


if __name__ == "__main__":
    task2()
    # main()
