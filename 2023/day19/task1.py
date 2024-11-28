import re


def predicate_builder(com_val, op):
    def gt(value):
        return value>com_val

    def lt(value):
        return value<com_val

    return gt if op==">" else lt


def fallback_builder(fallback):
    return lambda _: fallback


def rule_builder(category, predicate, rule_name, fall_trough):
    def inner_function(part):
        if predicate(part[category]):
            return rule_name
        else:
            return fall_trough(part)

    return inner_function


def main():
    with open("input", "r") as file:
        raw_workflows, ratings = file.read().split("\n\n")
        raw_workflows = raw_workflows.split("\n")
        ratings = ratings.split("\n")

    workflows = {}
    rule_pattern = re.compile(r"([a-z]+)([<|>])(\d+):([a-zA-Z]+)")
    for raw_workflow in raw_workflows:
        process_name, raw_rules = raw_workflow.split("{")
        *raw_rules, fallback = raw_rules[:-1].split(",")
        rule = fallback_builder(fallback)
        for raw_rule in reversed(raw_rules):
            rematch = re.fullmatch(rule_pattern, raw_rule)
            category = rematch.group(1)
            value = int(rematch.group(3))
            predicate = predicate_builder(value, rematch.group(2))
            rule = rule_builder(category, predicate, rematch.group(4), rule)

        workflows[process_name] = rule

    ratings = [
        {
            parts[0]: int(parts[1])
            for equation in line[1:-1].split(",")
            if (parts := equation.split("="))
        }
        for line in ratings
    ]

    ratings_sum = 0
    for rating in ratings:
        rule = "in"
        while rule not in ("A", "R"):
            rule = workflows[rule](rating)

        if rule == "A":
            ratings_sum += sum(rating.values())

    print(ratings_sum)


if __name__ == "__main__":
    main()
