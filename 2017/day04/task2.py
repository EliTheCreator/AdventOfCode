from collections import Counter


def main():
    with open("input", "r") as file:
        passphrases = [line.strip().split(" ") for line in file.readlines()]

    valid = 0
    for passphrase in passphrases:
        anagrams = set()
        for word in passphrase:
            counter = Counter(word)
            anagram = tuple(sorted(counter.items()))
            if anagram in anagrams:
                break
            else:
                anagrams.add(anagram)
        else:
            valid += 1

    print(valid)


if __name__ == "__main__":
    main()
