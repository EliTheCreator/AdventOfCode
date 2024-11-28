from re import findall


class Node():
    value: int
    prev: "Node"
    next: "Node"

    def __init__(self, value):
        self.value = value


def main():
    with open("input", "r") as file:
        data = [int(x) for x in findall(r"-?\d+", file.read())]

    first: Node = Node(data[0])
    first.prev = first
    first.next = first
    last: Node = first
    nodeIndex: dict[Node] = {}
    nodeIndex[0] = first
    zeroIndex = 0
    for index, value in enumerate(data[1:], 1):
        if value == 0:
            zeroIndex = index
        curNode = Node(value)
        nodeIndex[index] = curNode
        curNode.prev = last
        curNode.next = first
        first.prev = curNode
        last.next = curNode
        last = curNode

    for index in range(len(data)):
        cur: Node = nodeIndex[index]
        steps = cur.value%(len(data)-1)
        if steps == 0:
            continue

        prev = cur.prev
        next = cur.next

        prev.next = next
        next.prev = prev

        for _ in range(steps):
            next = next.next

        prev = next.prev
        prev.next = cur
        cur.prev = prev
        next.prev = cur
        cur.next = next

    total = 0
    cur: Node = nodeIndex[zeroIndex]
    steps = 1000%len(data)
    for _ in range(3):
        for _ in range(steps):
            cur = cur.next
        total += cur.value

    print(total)


if __name__ == "__main__":
    main()
