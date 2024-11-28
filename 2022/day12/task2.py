from collections import deque


def main():
    with open("input", "r") as file:
        heightmap = [[-100] + [ord(letter)-ord("a") for letter in line.strip()] + [-100] for line in file.readlines()]
        wall = [[-100 for _ in range(len(heightmap[0]))]]
        heightmap = wall + heightmap + wall

    end = None
    for y in range(1, len(heightmap)-1):
        for x in range(1, len(heightmap[0])-1):
            if heightmap[y][x] == ord("E")-ord("a"):
                end = (y, x)
        if end != None:
            break
    
    heightmap[end[0]][end[1]] = ord("z") - ord("a")
    visited = [[False for _ in range(len(heightmap[0]))] for _ in range(len(heightmap))]
    visited[end[0]][end[1]] = True

    queue = deque([(0, end)])
    while queue:
        steps, (curY, curX) = queue.popleft()
        curHeight = heightmap[curY][curX]
        if curHeight == 0:
            print(steps)
            return

        for dy, dx in ((1, 0), (0, 1), (0, -1), (-1, 0)):
            if not visited[curY+dy][curX+dx] and heightmap[curY+dy][curX+dx] >= curHeight-1:
                visited[curY+dy][curX+dx] = True
                queue.append((steps+1, (curY+dy, curX+dx)))


if __name__ == "__main__":
    main()
