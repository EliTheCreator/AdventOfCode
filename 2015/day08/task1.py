

def main():
    file = open("input", "r")
    lines = [line.strip() for line in file.readlines()]
    file.close()

    length = 0
    for line in lines:
        length += len(line) - len(eval(line))

    print(length)


if __name__ == "__main__":
    main()
