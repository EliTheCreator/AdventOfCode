

def main():
    with open("input", "r") as file:
        initialValue = int(file.readline().strip())

    value = initialValue
    round = 0
    offset = 1
    while value > 1:
        if value % 2:
            value += 1
            offset += 1 << round
        value //= 2
        round += 1

    print((1 - offset) % initialValue + 1)


if __name__ == "__main__":
    main()
