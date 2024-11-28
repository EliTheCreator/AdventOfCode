from itertools import cycle
from math import lcm
from functools import reduce


def main():
    with open("input", "r") as file:
        instructions = file.readline().strip()
        file.readline()
        nodes = dict([(line[0:3], (line[7:10], line[12:15])) for line in file.readlines()])

    start_nodes = [node for node in nodes.keys() if node.endswith("A")]
    cycle_lengths = []
    for start_node in start_nodes:
        steps = 0
        cur_node = start_node

        for instruction in cycle(instructions):
            if cur_node.endswith("Z"):
                cycle_lengths.append(steps)
                break

            match instruction:
                case "L":
                    cur_node = nodes[cur_node][0]
                case "R":
                    cur_node = nodes[cur_node][1]
                case _:
                    exit(1)

            steps += 1

    total_steps = reduce(lcm, cycle_lengths)
    print(total_steps)


if __name__ == "__main__":
    main()
