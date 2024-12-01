
def main():
    with open("input", "r") as file:
        data = [
            [int(elem) for elem in line.strip().split("   ")]
            for line in file.readlines()
        ]

    total_distance = 0
    for first, second in zip(*list(sorted(elem) for elem in zip(*data))):
        total_distance += abs(first-second)

    print(total_distance)


if __name__ == "__main__":
    main()
