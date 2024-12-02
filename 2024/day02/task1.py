
def main():
    with open("input", "r") as file:
        data = [[int(x) for x in line.strip().split(" ")] for line in file.readlines()]

    result = sum(
        (
            all(x>y and x<(y+4) for x, y in zip(line, line[1:]))
            or
            all(x<y and (x+4)>y for x, y in zip(line, line[1:]))
        )
        for line in data
    )

    print(result)


if __name__ == "__main__":
    main()
