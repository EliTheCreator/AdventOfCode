import re
from collections import defaultdict


def mirror(i, tile_size):
    n = 0
    for _ in range(tile_size):
        n <<= 1
        n += i % 2
        i >>= 1

    return n


def main():
    file = open("input", "r")
    raw_tiles = file.read().split("\n\n")
    file.close()

    tile_size = 0
    tiles = {}
    graph = defaultdict(lambda: set())
    tile_numbers = set()
    for raw_tile in raw_tiles:
        lines = raw_tile.split("\n")
        tile_size = len(lines[1])
        tile_number = int(re.findall(r"\d+", lines[0])[0])
        tile_numbers.add(tile_number)

        top = 0
        for c in lines[1]:
            top <<= 1
            if c == '#':
                top += 1

        right = 0
        for line in lines[1:]:
            c = line[-1]
            right <<= 1
            if c == '#':
                right += 1

        bottom = 0
        for shift, c in enumerate(lines[-1]):
            if c == '#':
                bottom += 1 << shift

        left = 0
        for shift, line in enumerate(lines[1:]):
            c = line[0]
            if c == '#':
                left += 1 << shift

        # tiles[tile_number] = [(x, mirror(x, tile_size))
        #                       for x in [top, right, bottom, left]]
        side_pairs = [(x, mirror(x, tile_size))
                      for x in [top, right, bottom, left]]
        sides, sides_mirrored = zip(*side_pairs)
        sides = set(sides)
        sides_mirrored = set(sides_mirrored)

        for first, second in side_pairs:
            graph[tile_number].add(first)
            graph[tile_number].add(second)
            graph[first].add(tile_number)
            graph[first].add(second)
            graph[second].add(tile_number)
            graph[second].add(first)

        for side in sides:
            graph[side] = graph[side].union(sides.difference([side]))

        for side in sides_mirrored:
            graph[side] = graph[side].union(sides.difference([side]))

    possible_corners = defaultdict(lambda: 0)
    for key in graph:
        if key < 1024 and len(graph[key]) == 5:
            possible_corners[max(graph[key])] += 1

    result = 1
    for key in possible_corners:
        if possible_corners[key] == 4:
            result *= key

    print(result)


if __name__ == "__main__":
    main()
