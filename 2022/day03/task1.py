
def to_val(char: str) -> int:
    if str.islower(char):
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 27


def main():
    with open("input", "r") as file:
        data = [(len(items)//2, items) for items in [line.strip() for line in file.readlines()]]

    common_letters = [set(items[:i]) & set(items[i:]) for i, items in data]
    print(sum([sum([to_val(letter) for letter in letters]) for letters in common_letters]))


if __name__ == "__main__":
    main()
