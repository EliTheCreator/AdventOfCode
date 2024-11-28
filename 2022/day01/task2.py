
def main():
    with open("input", "r") as file:
        data = file.read()

    result = sum(sorted([sum([int(x) for x in group.split("\n")]) for group in data.split("\n\n")])[-3:])
    print(result)


if __name__ == "__main__":
    main()
