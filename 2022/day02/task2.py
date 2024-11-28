
def points(pair: str) -> int:
    result: int = 0
    match pair:
        case "A X" | "B X" | "C X":
            result += 0
        case "A Y" | "B Y" | "C Y":
            result += 3
        case "A Z" | "B Z" | "C Z":
            result += 6
        case _:
            pass

    match pair:
        case "A Y" | "B X" | "C Z":
            result += 1
        case "A Z" | "B Y" | "C X":
            result += 2
        case "A X" | "B Z" | "C Y":
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
