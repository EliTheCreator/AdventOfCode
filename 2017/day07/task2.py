from collections import defaultdict


def main():
    graph = defaultdict(lambda: {})
    weights = {}
    with open("input", "r") as file:
        for line in file.readlines():
            parts = line.strip().split(" -> ")
            root, weight = parts[0].split(" ")
            weights[root] = int(weight[1:-1])
            if len(parts) > 1:
                for child in parts[1].split(", "):
                    graph[root][child] = 0

    def calcWeights(cur):
        subTreeWeights = []
        for next in graph[cur].keys():
            weight = calcWeights(next)
            graph[cur][next] = weight
            subTreeWeights.append(weight)

        weight = weights[cur] + sum(subTreeWeights)
        return weight

    def getCorrectedWeight(cur, expectedWeight):
        subTrees = sorted(graph[cur].items(), key=lambda x: x[1])
        if subTrees[0][1] != subTrees[1][1]:
            return getCorrectedWeight(subTrees[0][0], subTrees[1][1])
        elif subTrees[-2][1] != subTrees[-1][1]:
            return getCorrectedWeight(subTrees[-1][0], subTrees[-2][1])
        else:
            curWeigth = weights[cur]
            dif = expectedWeight - curWeigth - sum(graph[cur].values())
            return curWeigth + dif

    print(getCorrectedWeight("eugwuhl", calcWeights("eugwuhl")))


if __name__ == "__main__":
    main()
