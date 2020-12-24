import re
from itertools import permutations


def main():
    file = open("input", "r")
    tiles = [re.findall(r"e|se|sw|w|nw|ne", line) for line in file.readlines()]
    file.close()

    black_tiles = set()
    for tile in tiles:
        x, y, z = 0, 0, 0
        for direction in tile:
            if direction == 'e':
                x += 1
                y -= 1
            elif direction == 'w':
                x -= 1
                y += 1
            elif direction == 'ne':
                x += 1
                z -= 1
            elif direction == 'sw':
                x -= 1
                z += 1
            elif direction == 'nw':
                y += 1
                z -= 1
            elif direction == 'se':
                y -= 1
                z += 1

        if (x, y, z) in black_tiles:
            black_tiles.remove((x, y, z))
        else:
            black_tiles.add((x, y, z))

    for _ in range(100):
        new_black_tiles = set()
        to_check = set()
        for x, y, z in black_tiles:
            black_neighbours = 0
            for xo, yo, zo in permutations([-1, 0, 1]):
                tile = (x+xo, y+yo, z+zo)
                if tile in black_tiles:
                    black_neighbours += 1
                else:
                    to_check.add(tile)

            if 0 < black_neighbours < 3:
                new_black_tiles.add((x, y, z))

        for x, y, z in to_check:
            black_neighbours = 0
            for xo, yo, zo in permutations([-1, 0, 1]):
                tile = (x+xo, y+yo, z+zo)
                if tile in black_tiles:
                    black_neighbours += 1

            if black_neighbours == 2:
                new_black_tiles.add((x, y, z))

        black_tiles = new_black_tiles

    print(len(black_tiles))


if __name__ == "__main__":
    main()
