from enum import IntEnum, auto

class EnclosureState(IntEnum):
    NotIn = auto()
    NeedsUp = auto()
    NeedsDown = auto()
    IsIn = auto()


def main():
    with open("input", "r") as file:
        data = ["." + line + "." for line in file.readlines()]
        data = [["." for _ in data[0]]] + data + [["." for _ in data[0]]]

    type Node = tuple[int, int]
    graph: dict[Node, tuple[Node, Node]] = {}
    start_node: Node
    for row, line in enumerate(data[1:-1], 1):
        for col, letter in enumerate(line[1:-1], 1):
            match letter:
                case "|":
                    graph[(row,col)] = ((row-1,col),(row+1,col))
                case "-":
                    graph[(row,col)] = ((row,col-1),(row,col+1))
                case "L":
                    graph[(row,col)] = ((row-1,col),(row,col+1))
                case "J":
                    graph[(row,col)] = ((row-1,col),(row,col-1))
                case "7":
                    graph[(row,col)] = ((row+1,col),(row,col-1))
                case "F":
                    graph[(row,col)] = ((row+1,col),(row,col+1))
                case "S":
                    start_node = (row,col)
                case _:
                    pass

    prev_node: Node = start_node
    cur_node: Node
    neighbours = [False for _ in range(4)]
    for index, (dcol, drow) in enumerate(((-1,0), (1,0), (0,-1), (0,1))):
        col, row = prev_node
        neighbour = (col+dcol, row+drow)
        if neighbour in graph and prev_node in graph[neighbour]:
            cur_node = neighbour
            neighbours[index] = True

    pasture = [["." for _ in range(len(data[0]))] for _ in range(len(data))]
    while cur_node!=start_node:
        pasture[cur_node[0]][cur_node[1]] = data[cur_node[0]][cur_node[1]]
        n1, n2 = graph[cur_node]
        if n1 == prev_node:
            prev_node = cur_node
            cur_node = n2
        else:
            prev_node = cur_node
            cur_node = n1

    match neighbours:
        case [0,0,1,1]:
            pasture[start_node[0]][start_node[1]] = "|"
        case [0,1,0,1]:
            pasture[start_node[0]][start_node[1]] = "F"
        case [0,1,1,0]:
            pasture[start_node[0]][start_node[1]] = "L"
        case [1,0,0,1]:
            pasture[start_node[0]][start_node[1]] = "7"
        case [1,0,1,0]:
            pasture[start_node[0]][start_node[1]] = "J"
        case [1,1,0,0]:
            pasture[start_node[0]][start_node[1]] = "-"

    state = EnclosureState.NotIn
    enclosed_tiles = 0
    for line in pasture:
        for letter in line:
            match letter:
                case "|":
                    match state:
                        case EnclosureState.NotIn:
                            state = EnclosureState.IsIn
                        case EnclosureState.NeedsUp | EnclosureState.NeedsDown:
                            exit(1)
                        case EnclosureState.IsIn:
                            state = EnclosureState.NotIn
                case "-":
                    pass
                case "L":
                    match state:
                        case EnclosureState.NotIn:
                            state = EnclosureState.NeedsDown
                        case EnclosureState.NeedsUp | EnclosureState.NeedsDown:
                            exit(1)
                        case EnclosureState.IsIn:
                            state = EnclosureState.NeedsUp
                case "J":
                    match state:
                        case EnclosureState.NotIn | EnclosureState.IsIn:
                            exit(1)
                        case EnclosureState.NeedsUp:
                            state = EnclosureState.IsIn
                        case EnclosureState.NeedsDown:
                            state = EnclosureState.NotIn
                case "7":
                    match state:
                        case EnclosureState.NotIn | EnclosureState.IsIn:
                            exit(1)
                        case EnclosureState.NeedsUp:
                            state = EnclosureState.NotIn
                        case EnclosureState.NeedsDown:
                            state = EnclosureState.IsIn
                case "F":
                    match state:
                        case EnclosureState.NotIn:
                            state = EnclosureState.NeedsUp
                        case EnclosureState.NeedsUp | EnclosureState.NeedsDown:
                            exit(1)
                        case EnclosureState.IsIn:
                            state = EnclosureState.NeedsDown
                case ".":
                    if state == EnclosureState.IsIn:
                        enclosed_tiles += 1
                case _:
                    exit(1)

    print(enclosed_tiles)


if __name__ == "__main__":
    main()
