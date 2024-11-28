
def points(pair: str) -> int:
    result: int = 0
    match pair:
        case "A Y" | "B Z" | "C X":
            result += 6
        case "A X" | "B Y" | "C Z":
            result += 3
        case "A Z" | "B X" | "C Y":
            result += 0
        case _:
            pass

    match pair[-1]:
        case "X":
            result += 1
        case "Y":
            result += 2
        case "Z":
            result += 3
        case _:
            pass

    return result


def main():
    with open("input", "r") as file:
        data = [line.strip() for line in file.readlines()]

    print(sum(map(lambda pair: points(pair), data)))


if __name__ == "__main__":
    main()
