import re


def main():
    with open("input", "r") as file:
        data = [re.findall("[a-g]+", line.split("|")[1])
                for line in file.readlines()]

    print(sum((1 for line in data for num in line if len(num) in (2, 3, 4, 7))))


if __name__ == "__main__":
    main()
