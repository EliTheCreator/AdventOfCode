import re


def main():
    with open("input", "r") as file:
        positons = sorted([int(x) for x in re.findall("[0-9]+", file.read())])

    nCrabs = len(positons)
    median = positons[nCrabs // 2] if nCrabs % 2 == 1 else (
        positons[nCrabs // 2] + positons[nCrabs // 2 - 1]) // 2
    print(sum((abs(median - pos) for pos in positons)))


if __name__ == "__main__":
    main()
