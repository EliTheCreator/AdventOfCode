from hashlib import md5
from collections import deque
from operator import add


def main():
    with open("input", "r") as file:
        passcode = file.readline().strip()

    directionsAlph = ("U", "D", "L", "R")
    directionsNum = ((0, -1),
                     (0,  1),
                     (-1, 0),
                     (1,  0))
    target = (4, 4)
    rooms = ([0, 0, 0, 0, 0, 0],
             [0, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 0],
             [0, 0, 0, 0, 0, 0])

    queue = deque([((1, 1), "")])
    while queue:
        positinon, path = queue.popleft()
        if positinon == target:
            print(path)
            return
        permissions = md5((passcode + path).encode()).hexdigest()[:4]
        for i, permission in enumerate(permissions):
            if permission in "bcdef":
                x, y = map(add, positinon, directionsNum[i])
                if rooms[x][y]:
                    queue.append(((x, y), path + directionsAlph[i]))


if __name__ == "__main__":
    main()
