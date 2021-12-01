import os
import re


def main():
    file = open("input", "r")
    connections = [line.strip().split(" -> ") for line in file.readlines()]
    file.close()

    starts = set()
    for action, target in connections:
        action = action.split()
        length = len(action)
        if length == 1:
            start = action[0]
            starts.add(start)

        if 


    print(connections)


if __name__ == "__main__":
    main()
