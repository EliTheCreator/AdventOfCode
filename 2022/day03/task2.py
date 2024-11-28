
def to_val(char: str) -> int:
    if str.islower(char):
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 27


def main():
    with open("input", "r") as file:
        data = [line.strip() for line in file.readlines()]

    common_letters = []
    for i in range(0, len(data), 3):
        common_letters.append(set(data[i]) & set(data[i+1]) & set(data[i+2]))
    print(sum([sum([to_val(letter) for letter in letters]) for letters in common_letters]))


if __name__ == "__main__":
    main()