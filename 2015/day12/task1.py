import re


def main():
    with open("input", "r") as file:
        print(sum((int(x)
              for x in re.findall("-?\d+", file.read()))))


if __name__ == "__main__":
    main()
