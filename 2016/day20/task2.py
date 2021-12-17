

class Node():
    start: int
    end: int
    prev: 'Node'
    next: 'Node'

    def __init__(self, ipRange: tuple, prev: 'Node', next: 'Node'):
        self.start = ipRange[0]
        self.end = ipRange[1]
        self.prev = prev
        self.next = next

    def __str__(self):
        return f"{self.start} - {self.end}"


def main():
    with open("input", "r") as file:
        ipRanges = [[int(x) for x in line.strip().split("-")]
                    for line in file.readlines()]
    ipRanges.sort()

    rangesList: Node = None
    prevNode: Node = None
    for ipRange in ipRanges:
        newNode = Node(ipRange, prevNode, None)
        if prevNode is None:
            rangesList = newNode
        else:
            prevNode.next = newNode
        prevNode = newNode

    curNode = rangesList
    while curNode:
        nextNode = curNode.next
        if nextNode:
            if nextNode.start - 1 <= curNode.end:
                curNode.end = max(curNode.end, nextNode.end)
                curNode.next = nextNode.next
                if curNode.next:
                    curNode.next.prev = curNode
                continue

        curNode = nextNode

    allowed = 0
    curNode = rangesList
    while curNode:
        nextNode = curNode.next
        if nextNode:
            dif = nextNode.start - curNode.end - 1
            allowed += dif
        else:
            allowed += 4294967295 - curNode.end
        curNode = nextNode

    print(allowed)


if __name__ == "__main__":
    main()
