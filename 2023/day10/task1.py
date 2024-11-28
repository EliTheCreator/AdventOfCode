
def main():
    with open("input", "r") as file:
        data = ["." + line + "." for line in file.readlines()]
        data = [["." for _ in data[0]]] + data + [["." for _ in data[0]]]

    type Node = tuple[int, int]
    graph: dict[Node, tuple[Node, Node]] = {}
    path: list[Node] = []
    for j, line in enumerate(data[1:-1], 1):
        for i, letter in enumerate(line[1:-1], 1):
            match letter:
                case "|":
                    graph[(i,j)] = ((i,j-1),(i,j+1))
                case "-":
                    graph[(i,j)] = ((i-1,j),(i+1,j))
                case "L":
                    graph[(i,j)] = ((i,j-1),(i+1,j))
                case "J":
                    graph[(i,j)] = ((i,j-1),(i-1,j))
                case "7":
                    graph[(i,j)] = ((i,j+1),(i-1,j))
                case "F":
                    graph[(i,j)] = ((i,j+1),(i+1,j))
                case "S":
                    path.append((i,j))
                case _:
                    pass

    start_node: Node = path[-1]
    prev_node: Node = start_node
    cur_node: Node = None
    for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
        i, j = prev_node
        neighbour = (i+di, j+dj)
        if neighbour in graph and prev_node in graph[neighbour]:
            cur_node = neighbour
            break

    while cur_node!=start_node:
        path.append(cur_node)
        n1, n2 = graph[cur_node]
        if n1 == prev_node:
            prev_node = cur_node
            cur_node = n2
        else:
            prev_node = cur_node
            cur_node = n1

    print(len(path)//2)


if __name__ == "__main__":
    main()
