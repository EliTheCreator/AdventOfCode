from functools import reduce
import re


def main():
    with open("input", "r") as file:
        data = [tuple([line.split(" ")[0]] + [int(x) for x in re.findall("-?\d+", line)])
                for line in file.readlines()]

    scalars = [[row[i] for row in data] for i in range(1, len(data[0]))]

    maxSum = 0
    for w in range(100, -1, -1):
        for x in range(100 - w, -1, -1):
            for y in range(100 - w - x, -1, -1):
                z = 100 - w - x - y
                calories = sum(a*b for a, b in zip((w, x, y, z), scalars[-1]))
                if calories != 500:
                    continue

                def getScore(ingredient): return max(
                    0, sum(w * i for w, i in zip((w, x, y, z), ingredient)))

                curSum = reduce(lambda a, b: a*b, (getScore(ingredient)
                                for ingredient in scalars[:-1]))
                maxSum = max(curSum, maxSum)

    print(maxSum)


if __name__ == "__main__":
    main()
