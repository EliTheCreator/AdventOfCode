
def main():
    with open("input", "r") as file:
        puzzleInput = file.readline().strip()

    prev = puzzleInput
    next = ""
    for _ in range(50):
        cur = prev[0]
        counter = 1
        for c in prev[1:]:
            if c == cur:
                counter += 1
            else:
                next += str(counter) + cur
                cur = c
                counter = 1

        next += str(counter) + cur
        prev = next
        next = ""

    print(len(prev))


if __name__ == "__main__":
    main()
