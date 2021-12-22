from collections import defaultdict


def main():
    with open("input", "r") as file:
        destination = int(file.readline().strip())

    grid = defaultdict(lambda: 0, {((0, 0), 1)})

    neighbours = ((-1, -1), (0, -1), (1, -1),
                  (-1,  0), (1, 0),
                  (-1,  1), (0,  1), (1,  1))
    x, y = 0, 0
    dx, dy = 1, 1
    mx, my = 1, 1
    while True:
        for _ in range(dx):
            x += mx
            val = 0
            for ddx, ddy in neighbours:
                val += grid[(x + ddx, y + ddy)]
            if val > destination:
                print(val)
                return
            else:
                grid[(x, y)] = val
        dx += 1
        mx *= -1

        for _ in range(dy):
            y += my
            val = 0
            for ddx, ddy in neighbours:
                val += grid[(x + ddx, y + ddy)]
            if val > destination:
                print(val)
                return
            else:
                grid[(x, y)] = val
        dy += 1
        my *= -1


if __name__ == "__main__":
    main()
