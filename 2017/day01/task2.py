

def main():
    with open("input", "r") as file:
        data = file.readline().strip()

    count = 0
    l = len(data)
    h = l // 2
    for i in range(l):
        if data[i] == data[(i + h) % l]:
            count += int(data[i])

    print(count)


if __name__ == "__main__":
    main()
