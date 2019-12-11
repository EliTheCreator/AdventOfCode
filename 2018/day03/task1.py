import os


def main():
    file = open("input", "r")

    array = [[0 for y in range(1000)] for x in range(1000)]
    s = 0

    for line in file:
        _, _, from_cords, to_cords = line.split()
        fromx, fromy = from_cords.split(',')
        tox, toy = to_cords.split('x')

        fromx = int(fromx)
        tox = int(tox)
        fromy = int(fromy[:-1])
        toy = int(toy)

        for x in range(fromx, fromx+tox):
            for y in range(fromy, fromy+toy):
                if array[x][y] == 1:
                    s += 1
                array[x][y] += 1

    print(s)


main()
