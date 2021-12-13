from collections import defaultdict
from string import ascii_lowercase


def main():
    with open("input", "r") as file:
        data = [line.strip()[:-1].split("[") for line in file.readlines()]

    realRooms = []
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
            realRooms.append((name, sId))

    for name, sId in realRooms:
        translation = {ord("-"): " ", }

        for letter in ascii_lowercase:
            to = ((ord(letter) + sId) - ord("a")) % 26 + ord("a")
            translation[ord(letter)] = chr(to)

        if name.translate(translation) == "northpole object storage":
            print(sId)
            break


if __name__ == "__main__":
    main()
