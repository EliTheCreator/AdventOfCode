from enum import IntEnum


class Direction(IntEnum):
    _None = 0b0000
    Up = 0b0001
    Right = 0b0010
    Down = 0b0100
    Left = 0b1000


def main():
    with open("input", "r") as file:
        data = ['X' + line.strip() + 'X' for line in file.readlines()]
        data = ['X'*len(data[0])] + data + ['X'*len(data[0])]

    energized_tiles = [[Direction._None for _ in data[0]] for _ in data]
    stack = [((1,0), Direction.Right)]
    while stack:
        (row, col), direction = stack.pop()
        if energized_tiles[row][col] & direction:
            continue
        else:
            energized_tiles[row][col] |= direction

        match direction:
            case Direction._None:
                exit(-1)
            case Direction.Up:
                row -= 1
            case Direction.Right:
                col += 1
            case Direction.Down:
                row += 1
            case Direction.Left:
                col -= 1

        match data[row][col], direction:
            case ('X', _):
                pass
            case  ('.', _) \
                | ('|', Direction.Up) \
                | ('|', Direction.Down) \
                | ('-', Direction.Right) \
                | ('-', Direction.Left):
                stack.append(((row, col), direction))
            case  ('|', Direction.Right) \
                | ('|', Direction.Left):
                stack.append(((row, col), Direction.Up))
                stack.append(((row, col), Direction.Down))
            case  ('-', Direction.Up) \
                | ('-', Direction.Down):
                stack.append(((row, col), Direction.Right))
                stack.append(((row, col), Direction.Left))
            case ('/', Direction.Up):
                stack.append(((row, col), Direction.Right))
            case ('/', Direction.Right):
                stack.append(((row, col), Direction.Up))
            case ('/', Direction.Down):
                stack.append(((row, col), Direction.Left))
            case ('/', Direction.Left):
                stack.append(((row, col), Direction.Down))
            case ('\\', Direction.Up):
                stack.append(((row, col), Direction.Left))
            case ('\\', Direction.Right):
                stack.append(((row, col), Direction.Down))
            case ('\\', Direction.Down):
                stack.append(((row, col), Direction.Right))
            case ('\\', Direction.Left):
                stack.append(((row, col), Direction.Up))
            case _:
                exit(-1)

    print(sum(sum(tile!=Direction._None for tile in row) for row in energized_tiles)-1)


if __name__ == "__main__":
    main()
