from collections import defaultdict


def main():
    with open("input", "r") as file:
        data = [line.strip() for line in file.readlines()]

    data = [[row[i] for row in data] for i in range(len(data[0]))]
    message = []
    for line in data:
        frequnecy = defaultdict(lambda: 0)
        for letter in line:
            frequnecy[letter] += 1

        maxLetter, _ = min(frequnecy.items(), key=lambda x: x[1])
        message.append(maxLetter)

    print("".join(message))


if __name__ == "__main__":
    main()
