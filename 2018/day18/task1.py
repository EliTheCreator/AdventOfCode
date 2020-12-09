import os
import re
from copy import deepcopy


def main():
    file = open("input", "r")
    area = [[c for c in 'x' + line.strip() + 'x']
            for line in file.readlines()]
    file.close()
    filler = ['x' for _ in range(len(area[0]))]
    area.insert(0, filler)
    area.append(filler)

    for _ in range(10):
        temp_area = deepcopy(area)
        for i in range(1, len(area) - 1):
            for j in range(1, len(area[0]) - 1):
                openGround = 0
                trees = 0
                lumberyards = 0

                for oi in range(-1, 2):
                    for oj in range(-1, 2):
                        curAcre = temp_area[i+oi][j+oj]
                        if curAcre == '.':
                            openGround += 1
                        elif curAcre == '|':
                            trees += 1
                        elif curAcre == '#':
                            lumberyards += 1

                curAcre = temp_area[i][j]
                if curAcre == '.' and trees >= 3:
                    area[i][j] = '|'
                elif curAcre == '|' and lumberyards >= 3:
                    area[i][j] = '#'
                elif curAcre == '#' and (lumberyards < 2 or trees < 1):
                    area[i][j] = '.'

    trees = 0
    lumberyards = 0
    for line in area:
        for acre in line:
            if acre == '|':
                trees += 1
            elif acre == '#':
                lumberyards += 1

    print(trees * lumberyards)


if __name__ == "__main__":
    main()
