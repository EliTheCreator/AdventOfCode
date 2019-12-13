import itertools
import re


def main():
    file = open("input", "r")
    positions = [[int(x) for x in re.findall("-?[0-9]+", line)]
                 for line in file]
    velocities = [[0, 0, 0] for _ in range(len(positions))]
    file.close()

    combinations = list(itertools.combinations(range(len(positions)), 2))

    for _ in range(1000):
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

    totalEnergy = sum(sum(map(abs, pos)) * sum(map(abs, vel))
                      for pos, vel in zip(positions, velocities))

    print(totalEnergy)


if __name__ == "__main__":
    main()
