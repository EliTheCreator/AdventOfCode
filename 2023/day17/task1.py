from dataclasses import dataclass
from heapq import heappush, heappop, heapify


@dataclass
class Node:
    coords: tuple[int, int]
    direction: tuple[int, int]
    dir_steps: int
    distance: int

    def id(self) -> tuple[int, int, int, int, int]:
        return (*self.coords, *self.direction, self.dir_steps)

    def __lt__(self, other: "Node"):
        if self.distance > other.distance:
            return False
        elif self.distance == other.distance:
            return sum(self.coords) > sum(other.coords)
        else:
            return True


def main():
    with open("input", "r") as file:
        data = ['x' + line.strip() + 'x' for line in file.readlines()]
        data = ['x'*len(data[0])] + data + ['x'*len(data[0])]

    shortes_paths = {}
    visited = set()
    heap = []
    heapify(heap)
    heappush(heap, Node((1,1), (0,0), 0, 0))
    while heap:
        node: Node = heappop(heap)

        if node.coords == (len(data)-2, len(data[0])-2):
            print(node.distance)
            break

        visited.add(node.id())
        row, col = node.coords
        for d_row, d_col in ((-1,0), (1,0), (0,-1), (0,1)):
            if (d_row*-1, d_col*-1) == node.direction:
                continue

            new_dir_steps = node.dir_steps
            if (d_row, d_col) == node.direction:
                if new_dir_steps == 3:
                    continue
                else:
                    new_dir_steps += 1
            else:
                new_dir_steps = 1

            if (row+d_row, col+d_col, d_row, d_col, new_dir_steps) in visited:
                continue

            if data[row+d_row][col+d_col] == 'x':
                continue

            new_dist = node.distance + int(data[row+d_row][col+d_col])
            next_node = Node((row+d_row, col+d_col), (d_row, d_col), new_dir_steps, new_dist)
            if next_node.id() in shortes_paths:
                if shortes_paths[node.id()][0] > new_dist:
                    shortes_paths[next_node.id()] = (new_dist, node.id())
                else:
                    continue
            else:
                shortes_paths[next_node.id()] = (new_dist, node.id())

            heappush(heap, next_node)


if __name__ == "__main__":
    main()
