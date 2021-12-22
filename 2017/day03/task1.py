

def main():
    with open("input", "r") as file:
        destination = int(file.readline().strip()) - 1

    x, y = 0, 0
    dx, dy = 1, 1
    mx, my = 1, 1
    while True:
        if destination > 0:
            destination -= dx
            x += mx * dx
            mx *= -1
            dx += 1
        else:
            if my == -1:
                y += destination
            else:
                y -= destination
            break
        if destination > 0:
            destination -= dy
            y += my * dy
            my *= -1
            dy += 1
        else:
            if mx == -1:
                x += destination
            else:
                x -= destination
            break

    print(abs(x) + abs(y))


if __name__ == "__main__":
    main()
