from enum import IntEnum

class Direction(IntEnum):
    WE   = 0b1
    NWSE = 0b10
    NS   = 0b100
    NESW = 0b1000
    EW   = 0b10000
    SENW = 0b100000
    SN   = 0b1000000
    SWNE = 0b10000000


def main():
    with open("input", "r") as file:
        word_search = ["." + line.strip() + "." for line in file.readlines()]
        word_search = ["."*len(word_search[0])] + word_search + ["."*len(word_search[0])]

    offsets = (
        ( 0,-1),
        (-1,-1),
        (-1, 0),
        (-1, 1),
    )

    state = [[0 for _ in range(len(word_search[0]))] for _ in range(len(word_search))]
    xmas_count = 0
    for row in range(1, len(word_search)-1):
        for col in range(1, len(word_search[0])-1):
            match word_search[row][col]:
                case 'X':
                    for direction in list(Direction)[:4]:
                        state[row][col] |= direction
                    for (drow, dcol), direction in zip(offsets, list(Direction)[4:]):
                        if word_search[row+drow][col+dcol]=='M' and (state[row+drow][col+dcol]&direction):
                            xmas_count += 1
                case 'M':
                    for (drow, dcol), direction in zip(offsets, list(Direction)[:4]):
                        if word_search[row+drow][col+dcol]=='X' and (state[row+drow][col+dcol]&direction):
                            state[row][col] |= direction
                    for (drow, dcol), direction in zip(offsets, list(Direction)[4:]):
                        if word_search[row+drow][col+dcol]=='A' and (state[row+drow][col+dcol]&direction):
                            state[row][col] |= direction
                case 'A':
                    for (drow, dcol), direction in zip(offsets, list(Direction)[:4]):
                        if word_search[row+drow][col+dcol]=='M' and (state[row+drow][col+dcol]&direction):
                            state[row][col] |= direction
                    for (drow, dcol), direction in zip(offsets, list(Direction)[4:]):
                        if word_search[row+drow][col+dcol]=='S' and (state[row+drow][col+dcol]&direction):
                            state[row][col] |= direction
                case 'S':
                    for (drow, dcol), direction in zip(offsets, list(Direction)[:4]):
                        if word_search[row+drow][col+dcol]=='A' and (state[row+drow][col+dcol]&direction):
                            xmas_count += 1
                    for direction in list(Direction)[4:]:
                        state[row][col] |= direction
                case _:
                    pass

    print(xmas_count)


if __name__ == "__main__":
    main()
