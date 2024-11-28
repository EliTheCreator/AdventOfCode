
def main():
    with open("input", "r") as file:
        stream = file.read().strip()

    markerLength = 14

    uniqueLetters = 0
    curLetters = [0 for _ in range(ord('z') + 1)]
    for l in range(markerLength):
        letterNum = ord(stream[l])
        curLetters[letterNum] += 1
        if curLetters[letterNum] == 1:
            uniqueLetters += 1

    tail = 0
    head = markerLength
    while uniqueLetters < markerLength:
        tailLetterNum = ord(stream[tail])
        curLetters[tailLetterNum] -= 1
        if curLetters[tailLetterNum] == 0:
            uniqueLetters -= 1

        headLetterNum = ord(stream[head])
        curLetters[headLetterNum] += 1
        if curLetters[headLetterNum] == 1:
            uniqueLetters += 1

        head += 1
        tail += 1

    print(head)


if __name__ == "__main__":
    main()
