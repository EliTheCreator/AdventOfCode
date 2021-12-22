from collections import Counter


def main():
    with open("input", "r") as file:
        passphrases = [line.strip().split(" ") for line in file.readlines()]

    valid = 0
    for passphrase in passphrases:
        counter = Counter(passphrase)
        for num in counter.values():
            if num > 1:
                break
        else:
            valid += 1

    print(valid)


if __name__ == "__main__":
    main()
