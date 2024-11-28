
def main():
    with open("input", "r") as file:
        instructions = file.readline().split(",")

    total = 0
    for instruction in instructions:
        cur_total = 0
        for letter in instruction:
            cur_total += ord(letter)
            cur_total *= 17

        total += cur_total%256

    print(total)


if __name__ == "__main__":
    main()
