from collections import defaultdict, deque


def main():
    with open("input", "r") as file:
        _map = [[8] + [int(x) for x in line.strip()] + [8] for line in file.readlines()]
        _map = [[8]*len(_map[0])] + _map + [[8]*len(_map[0])]

    trailheads = []
    graph = defaultdict(set)
    for row, line in enumerate(_map[1:-1], 1):
        for col, number in enumerate(line[1:-1], 1):
            if number == 0:
                trailheads.append((row, col))
            for drow, dcol in ((-1,0),(1,0),(0,-1),(0,1)):
                if _map[row+drow][col+dcol] == number+1:
                    graph[(row, col)].add((row+drow, col+dcol))

    total = 0
    for trailhead in trailheads:
        queue = deque([trailhead])
        while queue:
            row, col = queue.popleft()
            if _map[row][col] == 9:
                total += 1
                continue

            for neighbour in graph[(row, col)]:
                queue.append(neighbour)

    print(total)


if __name__ == "__main__":
    main()
