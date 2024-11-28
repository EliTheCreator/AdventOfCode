
def main():
    with open("input", "r") as file:
        data = [[dict(pair.split(" ")[::-1] for pair in game.split(", "))
                for game in line.strip().split(": ", 1)[1].split("; ")]
                for line in file.readlines()]

    s = 0
    for index, game in enumerate(data, 1):
        possible = True
        for round in game:
            if not possible:
                break
            for color, number in ("red", 12), ("green", 13), ("blue", 14):
                if color in round and int(round[color]) > number:
                    possible = False
                    break

        if possible:
            s += index

    print(s)


if __name__ == "__main__":
    main()
