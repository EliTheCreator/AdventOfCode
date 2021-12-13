from collections import defaultdict


def main():
    with open("input", "r") as file:
        data = [line.strip()[:-1].split("[") for line in file.readlines()]

    sectorIdSum = 0
    for nameAndId, checksum in data:
        name = nameAndId[:-4]
        sId = int(nameAndId[-3:])

        letters = defaultdict(lambda: 0)
        for letter in name:
            if letter != "-":
                letters[letter] += 1

        nameVerification = zip(checksum, sorted(
            letters.items(), key=lambda k: (-k[1], k[0])))
        for cLetter, (nLetter, _) in nameVerification:
            if cLetter != nLetter:
                break
        else:
            sectorIdSum += sId

    print(sectorIdSum)


if __name__ == "__main__":
    main()
