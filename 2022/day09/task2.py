
def main():
    with open("input", "r") as file:
        motions = [(motion[0], int(motion[1])) for motion in [line.strip().split(" ") for line in file.readlines()]]

    numberOfKnots = 10
    knots = [[0, 0] for _ in range(numberOfKnots)]
    visited = set([(0, 0)])
    for directon, steps in motions:
        headMovement: tuple(int, int)
        match directon:
            case "U":
                headMovement = (0, 1)
            case "D":
                headMovement = (0, -1)
            case "L":
                headMovement = (-1, 0)
            case "R":
                headMovement = (1, 0)
            case _:
                headMovement = (0, 0)
        
        for _ in range(steps):
            knots[0][0] += headMovement[0]
            knots[0][1] += headMovement[1]

            for first, second in zip(range(0, numberOfKnots-1), range(1, numberOfKnots)):
                dy = knots[first][0] - knots[second][0]
                dx = knots[first][1] - knots[second][1]

                if abs(dy) == 2 or abs(dx) == 2:
                    if dy == 2:
                        knots[second][0] = knots[first][0] - 1
                    elif dy == -2:
                        knots[second][0] = knots[first][0] + 1
                    else:
                        knots[second][0] = knots[first][0]

                    if dx == 2:
                        knots[second][1] = knots[first][1] - 1
                    elif dx == -2:
                        knots[second][1] = knots[first][1] + 1
                    else:
                        knots[second][1] = knots[first][1]
                else:
                    break
            else:
                visited.add((knots[-1][0], knots[-1][1]))

    print(len(visited))


if __name__ == "__main__":
    main()
