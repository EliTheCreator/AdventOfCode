

def main():
    with open("input", "r") as file:
        state = [True if int(x) else False for x in file.readline().strip()]

    size = 272

    while len(state) <= size:
        b = [not x for x in reversed(state)]
        state += [False] + b

    checksum = [not state[i] ^ state[i+1] for i in range(0, size, 2)]
    while len(checksum) % 2 == 0:
        checksum = [not checksum[i] ^ checksum[i+1]
                    for i in range(0, len(checksum), 2)]

    print("".join("1" if x else "0" for x in checksum))


if __name__ == "__main__":
    main()
