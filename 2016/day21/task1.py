from collections import deque


def main():
    with open("input", "r") as file:
        instructions = [line.strip().split(" ") for line in file.readlines()]

    text = deque("abcdefgh")
    for line in instructions:
        match line:
            case "swap", "position", x, *_, y:
                x = int(x)
                y = int(y)
                temp = text[x]
                text[x] = text[y]
                text[y] = temp
            case "swap", "letter", x, *_, y:
                for i, c in enumerate(text):
                    if c == x:
                        text[i] = y
                    if c == y:
                        text[i] = x
            case "rotate", "left", x, *_:
                text.rotate(-int(x))
            case "rotate", "right", x, *_:
                text.rotate(int(x))
            case "rotate", "based", *_, x:
                i = 0
                for c in text:
                    if c != x:
                        i += 1
                    else:
                        break
                text.rotate(i + 1)
                if i >= 4:
                    text.rotate(1)
            case "reverse", _, x, _, y:
                x = int(x)
                y = int(y)
                reversedPart = [text[i] for i in range(x, y+1)]
                reversedPart.reverse()
                for i in range(y - x + 1):
                    text[x + i] = reversedPart[i]
            case "move", _, x, *_, y:
                c = text[int(x)]
                text.remove(c)
                text.insert(int(y), c)
            case _:
                pass

    print("".join(text))


if __name__ == "__main__":
    main()
