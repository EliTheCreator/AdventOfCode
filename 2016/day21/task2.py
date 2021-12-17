from collections import deque


def main():
    with open("input", "r") as file:
        instructions = [line.strip().split(" ") for line in file.readlines()]
    instructions.reverse()

    text = deque("fbgdceah")
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
                text.rotate(int(x))
            case "rotate", "right", x, *_:
                text.rotate(-int(x))
            case "rotate", "based", *_, x:
                rotations = [(2*i+1) % len(text) if i < 4 else (2*i+2) %
                             len(text) for i in range(len(text))]
                rotationsReversed = dict(
                    (rotations[i], i) for i in range(len(text)))
                i = 0
                for c in text:
                    if c != x:
                        i += 1
                    else:
                        break
                while text[rotationsReversed[i]] != x:
                    text.rotate(-1)
            case "reverse", _, x, _, y:
                x = int(x)
                y = int(y)
                reversedPart = [text[i] for i in range(x, y+1)]
                reversedPart.reverse()
                for i in range(y - x + 1):
                    text[x + i] = reversedPart[i]
            case "move", _, x, *_, y:
                c = text[int(y)]
                text.remove(c)
                text.insert(int(x), c)
            case _:
                pass

    print("".join(text))


if __name__ == "__main__":
    main()
