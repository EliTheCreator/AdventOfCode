from collections import defaultdict


def main():
    with open("input", "r") as file:
        lines = [line.strip().split(" ") for line in file.readlines()]

    paths = []
    sizes = defaultdict(lambda: 0)
    for line in lines:
        if line[0] == "$" and line[1] == "cd":
            if line[2] == "/":
                paths = ["/"]
            elif line[2] == "..":
                paths.pop()
            else:
                paths.append(paths[-1] + "/" + line[2])
        elif line[0].isdigit():
            for path in paths:
                sizes[path] += int(line[0])

    toFree = 30000000 - (70000000 - sizes["/"])
    print(min([folder for folder in sizes.items() if folder[1] >= toFree], key=lambda x: x[1])[1])


if __name__ == "__main__":
    main()
