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

    start_configurations = []
    row_tiles_count = len(data)-2
    col_tiles_count = len(data[0])-2
    for row in range(1, row_tiles_count+1):
        start_configurations.append(((row, 0), Direction.Right))
        start_configurations.append(((row, col_tiles_count+1), Direction.Left))
    for col in range(1, col_tiles_count+1):
        start_configurations.append(((0, col), Direction.Down))
        start_configurations.append(((row_tiles_count+1, col), Direction.Up))

    max_energized_tiles_count = 0
    for start_configuration in start_configurations:
        energized_tiles = [[Direction._None for _ in data[0]] for _ in data]
        stack = [start_configuration]
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

        energized_tiles_count = sum(sum(tile!=0 for tile in row) for row in energized_tiles)-1
        max_energized_tiles_count = max(max_energized_tiles_count, energized_tiles_count)

    print(max_energized_tiles_count)


if __name__ == "__main__":
    main()
