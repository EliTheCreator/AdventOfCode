from collections import deque
from string import digits


class Node:
    def __init__(self, t, value=None, parent=None):
        self.t = t
        self.value = value
        self.parent = parent
        self.middle = None
        self.left = None
        self.right = None


def main():
    file = open("input", "r")
    lines = [line.strip() for line in file.readlines()]
    file.close()

    s = 0
    for line in lines:
        # generate AST
        root = Node(0)
        cur_node = root
        for c in line:
            if c == ' ':
                continue
            elif c == '(':
                node = Node(1)
                if cur_node.t == 0:
                    root.middle = node
                    node.parent = root
                    cur_node = node
                elif cur_node.t == 1:
                    cur_node.middle = node
                    node.parent = cur_node
                    cur_node = node
                elif cur_node.t in (3, 4):
                    if cur_node.left is None:
                        cur_node.left = node
                    else:
                        cur_node.right = node
                    node.parent = cur_node
                    cur_node = node
                else:
                    assert False
            if c == ')':
                while cur_node.t != 1:
                    cur_node = cur_node.parent
                cur_node.t = 2
            elif c in ('+', '*'):
                node = None
                if c == '+':
                    node = Node(3)
                else:
                    node = Node(4)

                if cur_node.t in (2, 5):
                    node.left = cur_node
                    parent = cur_node.parent
                    cur_node.parent = node

                    node.parent = parent
                    if parent.left is not None and parent.left == cur_node:
                        parent.left = node
                    elif parent.right is not None and parent.right == cur_node:
                        parent.right = node
                    elif parent.middle is not None and parent.middle == cur_node:
                        parent.middle = node
                    else:
                        print(parent.middle)
                        assert False
                elif cur_node.t in (3, 4):
                    node.parent = cur_node
                    cur_node.right = node
                    cur_node = node

                else:
                    assert False

                cur_node = node
            elif c in digits:
                node = Node(5, int(c), cur_node)

                if cur_node.t in (0, 1):
                    cur_node.middle = node
                elif cur_node.t in (3, 4):
                    cur_node.right = node
                else:
                    assert False

                cur_node = node

        # push add nodes down
        stack = deque()
        stack.append(root)
        while stack:
            cur_node = stack.popleft()
            if cur_node.t == 3:
                if cur_node.right.t == 4:
                    parent = cur_node.parent
                    mul = cur_node.right
                    right = mul.left

                    mul.parent = parent
                    if parent.left is not None and parent.left == cur_node:
                        parent.left = mul
                    elif parent.right is not None and parent.right == cur_node:
                        parent.right = mul
                    elif parent.middle is not None and parent.middle == cur_node:
                        parent.middle = mul
                    else:
                        assert False

                    mul.left = cur_node
                    cur_node.parent = mul
                    cur_node.right = right
                    right.parent = cur_node

                    stack.append(parent)
                else:
                    stack.append(cur_node.left)
                    stack.append(cur_node.right)
            else:
                if cur_node.left is not None:
                    stack.append(cur_node.left)
                if cur_node.middle is not None:
                    stack.append(cur_node.middle)
                if cur_node.right is not None:
                    stack.append(cur_node.right)

        def solve(node):
            t = node.t
            if t in (0, 2):
                return solve(node.middle)
            elif t == 3:
                return solve(node.left) + solve(node.right)
            elif t == 4:
                return solve(node.left) * solve(node.right)
            if t == 5:
                return node.value
            else:
                print(t)
                assert False

        s += solve(root)

    print(s)


if __name__ == "__main__":
    main()
