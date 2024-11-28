from itertools import cycle


def main():
    with open("input", "r") as file:
        instructions = file.readline().strip()
        file.readline()
        nodes = dict([(line[0:3], (line[7:10], line[12:15])) for line in file.readlines()])

    cur_node = "AAA"
    target = "ZZZ"
    steps = 0
    for instruction in cycle(instructions):
        if cur_node == target:
            break

        steps += 1
        match instruction:
            case "L":
                cur_node = nodes[cur_node][0]
            case "R":
                cur_node = nodes[cur_node][1]
            case _:
                exit(1)

    print(steps)


if __name__ == "__main__":
    main()
