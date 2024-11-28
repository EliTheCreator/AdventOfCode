from collections import defaultdict
from dataclasses import dataclass
import re


@dataclass
class Node:
    predicate: tuple[str, str, int]
    to_pos: str
    to_neg: str

    def default():
        return Node(('x', '>', 0), None, None)


def main():
    with open("input", "r") as file:
        raw_workflows, _ = file.read().split("\n\n")
        raw_workflows = raw_workflows.split("\n")

    workflows = defaultdict(lambda: Node.default())

    rule_pattern = re.compile(r"([a-z]+)([<|>])(\d+):([a-zA-Z]+)")
    for raw_workflow in raw_workflows:
        process_name, raw_rules = raw_workflow.split("{")
        *raw_rules, to_neg = raw_rules[:-1].split(",")
        for index, raw_rule in enumerate(reversed(raw_rules)):
            rematch = re.fullmatch(rule_pattern, raw_rule)
            category = rematch.group(1)
            value = int(rematch.group(3))
            predicate = rematch.group(2)
            to_pos = rematch.group(4)
            node_name = f"{process_name}_{category}_{index}"

            workflows[node_name] = Node((category, predicate, value), to_pos, to_neg)

            to_neg = node_name

        workflows[process_name].to_pos = to_neg


    stack = []
    stack.append(('in', {'x':(1, 4000), 'm':(1, 4000), 'a':(1, 4000), 's':(1, 4000)}))

    solution_ranges = []
    while stack:
        node_name, ranges = stack.pop()
        if node_name is None:
            continue

        if node_name == 'A':
            solution_ranges.append((tuple(ranges.values())))
            continue
        elif node_name == 'R':
            continue

        ranges = ranges.copy()
        node = workflows[node_name]
        category, predicate, value = node.predicate
        _min, _max = ranges[category]
        if predicate == ">":
            n_min = max(_min, value+1)
            n_max = min(_max, value)

            if n_min<=_max:
                c_ranges = ranges.copy()
                c_ranges[category] = (n_min, _max)
                stack.append((node.to_pos, c_ranges))

            if _min<=n_max:
                ranges[category] = (_min, n_max)
                stack.append((node.to_neg, ranges))
        else:
            n_min = max(_min, value)
            n_max = min(_max, value-1)

            if _min<=n_max:
                c_ranges = ranges.copy()
                c_ranges[category] = (_min, n_max)
                stack.append((node.to_pos, c_ranges))

            if n_min<=_max:
                ranges[category] = (n_min, _max)
                stack.append((node.to_neg, ranges))

    total_solutions = 0
    for range in solution_ranges:
        product = 1
        for _min, _max in range:
            product *= _max-_min+1
        total_solutions += product

    print(total_solutions)


if __name__ == "__main__":
    main()
