from collections import deque
from string import digits


def main():
    file = open("input", "r")
    lines = [line.strip() for line in file.readlines()]
    file.close()

    def parse(i, line):
        queue = deque()
        c = line[i]
        while c != ')':
            if c == '(':
                i, value = parse(i+1, line)
                queue.append(value)
            elif c in digits:
                queue.append(int(c))
            elif c in "+*":
                queue.append(c)

            i += 1
            if i < len(line):
                c = line[i]
            else:
                break

        left = queue.popleft()
        while queue:
            op = queue.popleft()
            right = queue.popleft()
            if op == "+":
                left += right
            else:
                left *= right

        return (i, left)

    print(sum(map(lambda l: parse(0, l)[1], lines)))


if __name__ == "__main__":
    main()
