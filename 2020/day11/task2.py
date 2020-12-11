from copy import deepcopy
from hashlib import md5
from time import sleep


def check(lookup, i, j, iOffset, jOffset):
    _i = iOffset
    _j = jOffset

    while 0 < i + _i < len(lookup) and 0 < j + _j < len(lookup[0]):
        if lookup[i + _i][j + _j] == '#':
            return 1
        elif lookup[i + _i][j + _j] == 'L':
            return 0
        _i += iOffset
        _j += jOffset

    return 0


def main():
    file = open("input", "r")
    seating = [[c for c in '.' + line.strip() + '.']
               for line in file.readlines()]
    file.close()
    filler = ['.' for _ in range(len(seating[0]))]
    seating.insert(0, filler)
    seating.append(filler)

    iterations = set()
    iterations.add(md5(''.join([''.join(x)
                                for x in seating]).encode()).digest())
    while True:
        lookup = deepcopy(seating)
        for i in range(1, len(seating) - 1):
            for j in range(1, len(seating[0]) - 1):
                taken = 0
                taken += check(lookup, i, j, -1, 0)
                taken += check(lookup, i, j, -1, 1)
                taken += check(lookup, i, j, 0, 1)
                taken += check(lookup, i, j, 1, 1)
                taken += check(lookup, i, j, 1, 0)
                taken += check(lookup, i, j, 1, -1)
                taken += check(lookup, i, j, 0, -1)
                taken += check(lookup, i, j, -1, -1)

                seat = lookup[i][j]
                if seat == 'L' and taken == 0:
                    seating[i][j] = '#'
                elif seat == '#' and taken > 4:
                    seating[i][j] = 'L'

        hashed = md5(''.join(['\n'.join(x)
                              for x in seating]).encode()).digest()
        if hashed in iterations:
            taken = sum([len(list(filter(lambda c: c == '#', row)))
                         for row in seating])
            print(taken)
            break
        else:
            iterations.add(hashed)


if __name__ == "__main__":
    main()
