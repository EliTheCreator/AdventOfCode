import heapq
import re


def main():
    with open("input", "r") as file:
        grid = [[int(x) for x in re.findall(r"\d", line)]
                for line in file.readlines()]

    xSize, ySize = (len(grid), len(grid[0]))
    target = (xSize - 1, ySize - 1)
    neighbours = ((-1, 0), (1, 0),
                  (0, -1), (0, 1))

    def legal(coords):
        x, y = coords
        if x < 0 or xSize <= x:
            return False
        if y < 0 or ySize <= y:
            return False
        return True

    heap = [(0, (0, 0))]
    heapq.heapify(heap)
    visited = set()
    while heap:
        curRisk, (x, y) = heapq.heappop(heap)
        if (x, y) == target:
            print(curRisk)
            return
        if (x, y) not in visited:
            visited.add((x, y))
            for dx, dy in neighbours:
                nx, ny = (x + dx, y + dy)
                if legal((nx, ny)) and (nx, ny) not in visited:
                    newRisk = curRisk + grid[nx][ny]
                    heapq.heappush(heap, (newRisk, (nx, ny)))


if __name__ == "__main__":
    main()
