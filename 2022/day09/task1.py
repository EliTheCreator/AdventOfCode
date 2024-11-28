
def main():
    with open("input", "r") as file:
        motions = [(motion[0], int(motion[1])) for motion in [line.strip().split(" ") for line in file.readlines()]]

    headPositon = [0, 0]
    tailPositon = [0, 0]
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
            headPositon[0] += headMovement[0]
            headPositon[1] += headMovement[1]

            dy = headPositon[0] - tailPositon[0]
            dx = headPositon[1] - tailPositon[1]
            match (dy, dx):
                case (2, _):
                    tailPositon[0] = headPositon[0] - 1
                    tailPositon[1] = headPositon[1]
                case (-2, _):
                    tailPositon[0] = headPositon[0] + 1
                    tailPositon[1] = headPositon[1]
                case (_, 2):
                    tailPositon[0] = headPositon[0]
                    tailPositon[1] = headPositon[1] - 1
                case (_, -2):
                    tailPositon[0] = headPositon[0]
                    tailPositon[1] = headPositon[1] + 1
                case _:
                    continue
            
            visited.add((tailPositon[0], tailPositon[1]))
    
    print(len(visited))


if __name__ == "__main__":
    main()
