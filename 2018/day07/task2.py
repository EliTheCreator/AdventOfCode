import re


def main():
    file = open("input", "r")
    edges = [[x.strip() for x in re.findall(" [A-Z] ", line)] for line in file]
    file.close()

    tree = {}
    isRoot = set([x[0] for x in edges] + [x[1] for x in edges])

    tree = {}
    inDegree = {}
    for vertex in isRoot:
        tree[vertex] = set()
        inDegree[vertex] = 0

    for fro, to in edges:
        if to in isRoot:
            isRoot.remove(to)
        tree[fro].add(to)
        inDegree[to] += 1

    avSet = isRoot
    av = sorted(avSet)
    solution = []

    steps = -1
    letter = ["", "", "", "", ""]
    delay = [0, 0, 0, 0, 0]
    while len(solution) < 26:
        steps += 1
        for worker in range(5):
            if delay[worker] == 0:
                if letter[worker] != "":
                    # print(f"{steps} {letter[worker]}")
                    solution.append(letter[worker])
                    for child in tree[letter[worker]]:
                        if inDegree[child] == 1:
                            avSet.add(child)
                        else:
                            inDegree[child] -= 1

                    letter[worker] = ""
                if av:
                    vertex = av.pop(0)
                    avSet.remove(vertex)
                    letter[worker] = vertex
                    delay[worker] = ord(vertex) - 5
                    # print(f"Starting {letter[worker]} at {steps}")

                av = sorted(avSet)
            else:
                delay[worker] -= 1

        for worker in range(5):
            if delay[worker] == 0 and letter[worker] == "" and av:
                vertex = av.pop(0)
                avSet.remove(vertex)
                letter[worker] = vertex
                delay[worker] = ord(vertex) - 5
                # print(f"Starting {letter[worker]} at {steps}")

    print(steps)


main()
