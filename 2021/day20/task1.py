from collections import defaultdict
from itertools import product


def main():
    with open("input", "r") as file:
        codeRaw, _, *imageRaw = file.read().split("\n")

    code = ['1' if c == '#' else '0' for c in codeRaw]

    default = '0'
    image = defaultdict(lambda: default)
    for x in range(len(imageRaw)):
        for y in range(len(imageRaw[0])):
            image[(x, y)] = '1' if imageRaw[x][y] == '#' else '0'

    nextImage = defaultdict(lambda: code[int(9 * default, 2)])

    minC = -1
    maxC = max(len(imageRaw), len(imageRaw[0])) + 1

    for _ in range(2):
        for x in range(minC, maxC):
            for y in range(minC, maxC):
                index = ""
                for dx, dy in product((-1, 0, 1), repeat=2):
                    index += image[(x + dx, y + dy)]
                nextImage[(x, y)] = code[int(index, 2)]

        temp = image
        image = nextImage
        nextImage = temp
        minC -= 1
        maxC += 1

    lightPixels = 0
    for x in range(minC, maxC):
        for y in range(minC+1, maxC-1):
            lightPixels += int(image[(x, y)])

    print(lightPixels)


if __name__ == "__main__":
    main()
