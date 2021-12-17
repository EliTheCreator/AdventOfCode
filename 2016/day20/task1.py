

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

    mergedRanges: Node = None
    for start, end in ipRanges:
        prev: Node = None
        cur: Node = mergedRanges
        found = False

        # This loop contains a bug somewhere
        while cur and not found:
            found = True
            if end < cur.start - 1:
                newNode = Node((start, end), cur.prev, cur)
                if cur.prev is None:
                    mergedRanges = newNode
                else:
                    cur.prev.next = newNode
                cur.prev = newNode
            elif cur.start - 1 <= end and end <= cur.end:
                if start < cur.start:
                    cur.start = start
            elif start - 1 <= cur.end and cur.end < end:
                if start < cur.start:
                    cur.start = start
                if cur.next and cur.next.start - 1 <= end:
                    next: Node = cur.next
                    cur.end = next.end
                    cur.next = next.next
                    if cur.next:
                        cur.next.prev = cur
                else:
                    cur.end = end
            else:
                found = False
                prev = cur
                cur = cur.next

        if not found:
            newNode = Node((start, end), prev, None)
            if prev is None:
                mergedRanges = newNode
            else:
                prev.next = newNode

    if mergedRanges.start > 0:
        print(0)
    else:
        print(mergedRanges.end + 1)


if __name__ == "__main__":
    main()
