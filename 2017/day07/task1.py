

def main():
    graph = {}
    with open("input", "r") as file:
        for line in file.readlines():
            parts = line.strip().split(" -> ")
            root = parts[0].split(" ")[0]
            if len(parts) > 1:
                for child in parts[1].split(", "):
                    graph[child] = root

    node = list(graph.keys())[0]
    while node in graph.keys():
        node = graph[node]

    print(node)


if __name__ == "__main__":
    main()
