
def main():
    with open("input", "r") as file:
        data = [[int(x) for x in line.strip().split(" ")] for line in file.readlines()]

    result = 0
    for line in data:
        for index in range(len(line)):
            sub_line = line[:index] + line[index+1:]

            condition = (
                all(x>y and x<(y+4) for x, y in zip(sub_line, sub_line[1:]))
                or
                all(x<y and (x+4)>y for x, y in zip(sub_line, sub_line[1:]))
            )

            if condition:
                result += 1
                break

    print(result)


if __name__ == "__main__":
    main()
