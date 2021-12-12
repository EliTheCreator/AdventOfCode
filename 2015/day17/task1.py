import re


def rec(eggnog, containers):
    combinations = 0
    if containers:
        combinations += rec(eggnog, containers[1:])
        leftEggnog = eggnog - containers[0]
        if leftEggnog > 0:
            combinations += rec(leftEggnog, containers[1:])
        elif leftEggnog == 0:
            combinations += 1

    return combinations


def main():
    with open("input", "r") as file:
        containers = tuple(
            sorted([int(x) for x in re.findall("\d+", file.read())], reverse=True))

    print(rec(150, containers))


if __name__ == "__main__":
    main()
