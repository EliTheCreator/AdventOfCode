
def main():
    with open("input", "r") as file:
        instructions = [line.strip().split() for line in file.readlines()]

    rows = 6
    cols = 40
    screen = ["." for _ in range(rows * cols)]
    cycle = 0
    x = 1
    for instruction in instructions:
        pixel = "."
        if x-1 <= cycle%cols and cycle%cols <= x+1:
            pixel = "#"

        screen[(cycle//cols)*cols + (cycle%cols)] = pixel
        cycle += 1

        match instruction[0]:
            case "addx":
                pixel = "."
                if x-1 <= cycle%cols and cycle%cols <= x+1:
                    pixel = "#"

                screen[(cycle//cols)*cols + (cycle%cols)] = pixel
                cycle += 1

                x += int(instruction[1])
            case _:
                pass

    for row in range(rows):
        for col in range(cols):
            print(screen[row*cols + col], end="")
        print()


if __name__ == "__main__":
    main()
