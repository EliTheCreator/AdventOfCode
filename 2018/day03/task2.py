import os
import re


def main():
    file = open("input", "r")

    array = [[0 for y in range(1000)] for x in range(1000)]
    elfs = [True for x in range(1412)]

    for line in file:
        elf_id, fromx, fromy, tox, toy = [
            int(x) for x in re.findall("[0-9]+", line)]

        for x in range(fromx, fromx+tox):
            for y in range(fromy, fromy+toy):
                if array[x][y] == 0:
                    array[x][y] = elf_id
                else:
                    elfs[elf_id] = False
                    elfs[array[x][y]] = False

    file.close()

    for x in range(1, 1412):
        if elfs[x]:
            print(x)
            return


main()
