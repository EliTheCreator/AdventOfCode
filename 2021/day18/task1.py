from functools import reduce


class TreeElement():
    pass


class Node(TreeElement):
    parent: 'Node'
    left: TreeElement
    right: TreeElement

    def __init__(self, parent: 'Node', left: TreeElement = None, right: TreeElement = None):
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left},{self.right})"


class Leaf(TreeElement):
    value: int

    def __init__(self, value: int):
        self.value = value

    def __str__(self):
        return str(self.value)


def main():
    def scan(line, parent):
        node = Node(parent)
        left, right = None, None
        i = 1
        if line[i] == "[":
            left, offset = scan(line[i:], node)
            i += offset
        else:
            left = Leaf(int(line[i]))
            i += 1
        i += 1
        if line[i] == "[":
            right, offset = scan(line[i:], node)
            i += offset
        else:
            right = Leaf(int(line[i]))
            i += 1
        i += 1

        node.left = left
        node.right = right

        return node, i

    def explodeReduce(node: Node, depth):
        depth += 1
        reduced = False
        match node.left, node.right:
            case Leaf() as left, Leaf() as right:
                if depth > 4:
                    cur = node
                    parent = node.parent
                    while parent is not None and parent.left == cur:
                        cur = parent
                        parent = cur.parent
                    if parent is not None:
                        cur = parent.left
                        while not isinstance(cur, Leaf):
                            cur = cur.right
                        cur.value += left.value

                    cur = node
                    parent = node.parent
                    while parent is not None and parent.right == cur:
                        cur = parent
                        parent = cur.parent
                    if parent is not None:
                        cur = parent.right
                        while not isinstance(cur, Leaf):
                            cur = cur.left
                        cur.value += right.value

                    leaf = Leaf(0)
                    parent = node.parent
                    if parent.left == node:
                        parent.left = leaf
                    else:
                        parent.right = leaf
                    reduced = True
            case Node() as left, Leaf() as right:
                reduced = explodeReduce(left, depth)
            case Leaf() as left, Node() as right:
                reduced = explodeReduce(right, depth)
            case Node() as left, Node() as right:
                reduced = explodeReduce(left, depth)
                if not reduced:
                    reduced = explodeReduce(right, depth)

        return reduced

    def split(parent: Node, node: Node):
        left = Leaf(node.value // 2)
        right = Leaf((node.value + 1) // 2)
        return Node(parent, left, right)

    def splitReduce(node: Node):
        reduced = False
        match node.left, node.right:
            case Leaf() as left, Leaf() as right:
                if left.value > 9:
                    node.left = split(node, left)
                    reduced = True
                if not reduced and right.value > 9:
                    node.right = split(node, right)
                    reduced = True
            case Node() as left, Leaf() as right:
                reduced = splitReduce(left)
                if not reduced and right.value > 9:
                    node.right = split(node, right)
                    reduced = True
            case Leaf() as left, Node() as right:
                if left.value > 9:
                    node.left = split(node, left)
                    reduced = True
                if not reduced:
                    reduced = splitReduce(right)
            case Node() as left, Node() as right:
                reduced = splitReduce(left)
                if not reduced:
                    reduced = splitReduce(right)

        return reduced

    def reduceTree(node: Node):
        reduced = explodeReduce(node, 0)
        if not reduced:
            reduced = splitReduce(node)
        return reduced

    def addition(left: Node, right: Node):
        tree = Node(None, left, right)
        left.parent = tree
        right.parent = tree
        shouldReduce = True
        while shouldReduce:
            shouldReduce = reduceTree(tree)
        return tree

    def magnitude(tree: Node):
        leftVal = 0
        rightVal = 0

        match tree.left:
            case Leaf() as left:
                leftVal = left.value
            case Node() as left:
                leftVal = magnitude(left)

        match tree.right:
            case Leaf() as right:
                rightVal = right.value
            case Node() as right:
                rightVal = magnitude(right)

        return (3 * leftVal) + (2 * rightVal)

    with open("input", "r") as file:
        trees = [scan(line.strip(), None)[0] for line in file.readlines()]

    result = magnitude(reduce(addition, trees))
    print(result)


if __name__ == "__main__":
    main()
