
def main():
    active = set()
    file = open("input", "r")
    for x, line in enumerate(file.readlines()):
        for y, field in enumerate(line.strip()):
            if field == '#':
                active.add((x, y, 0, 0))
    file.close()

    for _ in range(6):
        to_check = set()
        next_active = set()

        for x, y, z, w in active:
            active_count = 0
            for xo in range(-1, 2):
                for yo in range(-1, 2):
                    for zo in range(-1, 2):
                        for wo in range(-1, 2):
                            if (x+xo, y+yo, z+zo, w+wo) in active:
                                active_count += 1
                            else:
                                to_check.add((x+xo, y+yo, z+zo, w+wo))

            if 2 < active_count < 5:
                next_active.add((x, y, z, w))

        for x, y, z, w in to_check:
            active_count = 0
            for xo in range(-1, 2):
                for yo in range(-1, 2):
                    for zo in range(-1, 2):
                        for wo in range(-1, 2):
                            if (x+xo, y+yo, z+zo, w+wo) in active:
                                active_count += 1

            if active_count == 3:
                next_active.add((x, y, z, w))

        active = next_active

    print(len(active))


if __name__ == "__main__":
    main()
