

def main():
    file = open("input", "r")
    lines = [line.strip() for line in file.readlines()]
    file.close()

    new_length = 0
    for line in lines:
        line_length = 2
        line_length += line.count("\\")
        line_length += line.count('"')
        new_length += line_length

    print(new_length)


if __name__ == "__main__":
    main()
