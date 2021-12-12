

def main():
    with open("clues", "r") as file:
        clues = [(k, int(v)) for k, v in [line.strip().split(": ")
                                          for line in file.readlines()]]

    with open("input", "r") as file:
        sues = [dict((k, int(v)) for k, v in [thing.split(":") for thing in line.split(":", maxsplit=1)[1].strip().split(", ")])
                for line in file.readlines()]

    for num, sue in enumerate(sues, 1):
        for item, quantity in clues:
            if item in sue:
                if quantity != sue[item]:
                    break
        else:
            print(num)
            break


if __name__ == "__main__":
    main()
