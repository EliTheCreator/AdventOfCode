from collections import defaultdict
from collections import deque


def main():
    file = open("input", "r")
    regex = file.readline().strip()
    file.close()

    bracketPairs = {}
    graph = defaultdict(lambda: set())

    def bracketMatch(i):
        while regex[i] != '(' and i < len(regex) - 1:
            i += 1

        start = i
        i += 1
        while regex[i] != ')':
            if regex[i] == '(':
                i = bracketMatch(i)
            else:
                i += 1
        end = i
        bracketPairs[start] = end
        return i + 1

    def follow(i, r, c):
        while i < len(regex) and regex[i] in ['N', 'S', 'E', 'W']:
            cr = regex[i]
            tr, tc = r, c
            if cr == 'N':
                tr += 1
            elif cr == 'S':
                tr -= 1
            elif cr == 'E':
                tc += 1
            elif cr == 'W':
                tc -= 1
            graph[(r, c)].add((tr, tc))
            graph[(tr, tc)].add((r, c))
            r, c = tr, tc
            i += 1

        if regex[i] == '(':
            end = bracketPairs[i]
            i += 1
            follow(i, r, c)
            while i < end:
                if regex[i] == '(':
                    i = bracketPairs[i] + 1
                elif regex[i] == '|':
                    i += 1
                    if regex[i] != ')':
                        follow(i, r, c)
                    else:
                        follow(i+1, r, c)
                        return
                else:
                    i += 1
        else:
            return

    i = 0
    while i < len(regex) - 1:
        i = bracketMatch(i)

    follow(1, 0, 0)

    visited = set()
    toVisit = deque([((0, 0), 0)])
    maxDist = 0
    while toVisit:
        curNode, dist = toVisit.popleft()
        visited.add(curNode)
        if dist >= 1000:
            maxDist += 1
        for child in graph[curNode]:
            if child not in visited:
                toVisit.append((child, dist+1))

    print(maxDist)

    # minR = min(graph.keys(), key=lambda a: a[0])[0]
    # maxR = max(graph.keys(), key=lambda a: a[0])[0]
    # minC = min(graph.keys(), key=lambda a: a[1])[1]
    # maxC = max(graph.keys(), key=lambda a: a[1])[1]

    # base = [['#' for _ in range(2*minC, 2*maxC + 3)]
    #         for _ in range(2*minR, 2*maxR + 3)]
    # rooms = graph.keys()
    # doors = set()
    # for room in rooms:
    #     doors = doors.union(graph[room])

    # for r in range(minR, maxR+1):
    #     for c in range(minC, maxC+1):
    #         if (r, c) in rooms:
    #             base[2*(abs(minR) + r) + 1][2*(abs(minC) + c) + 1] = '.'
    #             if (r, c+1) in doors:
    #                 base[2*(abs(minR) + r) + 1][2*(abs(minC) + c) + 2] = '|'
    #             if (r+1, c) in doors:
    #                 base[2*(abs(minR) + r) + 2][2*(abs(minC) + c) + 1] = '-'

    # base[1 + 2*abs(minR)][1 + 2*abs(minC)] = 'X'

    # for line in base:
    #     print(''.join(line))


if __name__ == "__main__":
    main()
