from collections import defaultdict
from functools import cmp_to_key
import re


def main():
    with open("input", "r") as file:
        rules, page_sets = file.read().split("\n\n")

    rules = [[int(x) for x in re.findall(r"\d+", line)] for line in rules.split("\n")]
    page_sets = [[int(x) for x in re.findall(r"\d+", line)] for line in page_sets.split("\n")]

    graph = defaultdict(lambda: set())
    for first, second in rules:
        graph[first].add(second)

    total = 0
    for page_set in page_sets:
        is_correct = True
        for i in range(len(page_set)):
            for j in range(i+1, len(page_set)):
                if page_set[j] not in graph[page_set[i]]:
                    is_correct = False
                    break

            if not is_correct:
                break

        if is_correct:
            continue

        page_set.sort(key=cmp_to_key(lambda x,y: 1 if x in graph[y] else -1))
        total += page_set[len(page_set)//2]

    print(total)


if __name__ == "__main__":
    main()
