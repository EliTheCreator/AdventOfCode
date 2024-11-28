
def main():
    with open("input", "r") as file:
        data = [[dict(pair.split(" ")[::-1] for pair in game.split(", "))
                for game in line.strip().split(": ", 1)[1].split("; ")]
                for line in file.readlines()]

    s = 0
    for game in data:
        red, green, blue = (0, 0, 0)
        for round in game:
            if "red" in round and int(round["red"]) > red:
                red = int(round["red"])
            if "green" in round and int(round["green"]) > green:
                green = int(round["green"])
            if "blue" in round and int(round["blue"]) > blue:
                blue = int(round["blue"])

        s += (red*green*blue)

    print(s)


if __name__ == "__main__":
    main()
