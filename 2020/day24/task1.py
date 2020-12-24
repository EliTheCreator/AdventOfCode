import re


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

    print(len(black_tiles))


if __name__ == "__main__":
    main()
