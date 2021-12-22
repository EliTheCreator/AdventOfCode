

def main():
    with open("input", "r") as file:
        data = file.readline().strip()

    count = int(data[0]) if data[0] == data[-1] else 0
    for a, b in zip(data, data[1:]):
        count += int(a) if a == b else 0

    print(count)


if __name__ == "__main__":
    main()
