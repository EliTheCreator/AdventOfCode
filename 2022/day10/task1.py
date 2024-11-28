
def main():
    with open("input", "r") as file:
        instructions = [line.strip().split() for line in file.readlines()]

    keyCycles = set([x+20 for x in range(0, 201, 40)])
    cycle = 1
    x = 1
    signalStrength = 0
    for instruction in instructions:
        if cycle in keyCycles:
            signalStrength += cycle * x
        cycle += 1

        match instruction[0]:
            case "addx":
                if cycle in keyCycles:
                    signalStrength += cycle * x
                cycle += 1
                x += int(instruction[1])
            case _:
                pass

    print(signalStrength)


if __name__ == "__main__":
    main()
