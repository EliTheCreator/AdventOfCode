from collections import deque
from itertools import permutations


def main():
    with open("input", "r") as file:
        maze = [[char for char in line.strip()] for line in file.readlines()]

    numbers = "0123456789"
    locations = {}
    for row, line in enumerate(maze):
        for col, char in enumerate(line):
            if char in numbers:
                locations[char] = (row, col)

    distances = {}

    for number, location in locations.items():
        queue = deque()
        curDistances = {}
        queue.append((location, 0))
        visited = set()
        while queue:
            (x, y), distance = queue.popleft()
            if (x, y) not in visited:
                visited.add((x, y))
                if maze[x][y] in numbers:
                    curDistances[maze[x][y]] = distance

                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) not in visited and maze[nx][ny] != '#':
                        queue.append(((nx, ny), distance + 1))

        distances[number] = curDistances

    minDist = 1000000
    destinations = set(locations.keys())
    destinations.difference_update(('0'))
    for permutation in permutations(destinations, len(destinations)):
        permutation = ['0'] + list(permutation) + ['0']
        curDist = 0
        for i in range(len(permutation) - 1):
            curDist += distances[permutation[i]][permutation[i + 1]]

        minDist = min(curDist, minDist)

    print(minDist)


if __name__ == "__main__":
    main()
