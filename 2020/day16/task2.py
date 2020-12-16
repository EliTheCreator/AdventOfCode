import re


def main():
    file = open("input", "r")
    raw_rules, raw_ticket, raw_tickets = file.read().split("\n\n")
    file.close()

    rule_names, rules = zip(*[line.split(":")
                              for line in raw_rules.splitlines()])
    rules = [[int(x) for x in re.findall(r"\d+", line)]
             for line in rules]
    personal_ticket = [int(x) for x in re.findall(
        r"\d+", raw_ticket.splitlines()[1])]
    nearby_tickets = [[int(x) for x in re.findall(r"\d+", line)]
                      for line in raw_tickets.splitlines()[1:]]

    nearby_tickets.append(personal_ticket)

    possible_translations = [[] for _ in range(len(rules))]
    for ticket in nearby_tickets:
        valid = True
        possible_rules_per_value = [set() for _ in range(len(ticket))]
        for value_num, value in enumerate(ticket):
            possible_rules = set()
            for rule_num, (r1l, r1h, r2l, r2h) in enumerate(rules):
                if r1l <= value <= r1h or r2l <= value <= r2h:
                    possible_rules.add(rule_num)

            if possible_rules:
                possible_rules_per_value[value_num] = possible_rules
            else:
                valid = False
                break

        if valid:
            for rule_num, possible_rules_set in enumerate(possible_rules_per_value):
                possible_translations[rule_num].append(
                    possible_rules_set)

    s0 = set([x for x in range(len(rules))])
    possible_translations = [(i, s0.intersection(*sets))
                             for i, sets in enumerate(possible_translations)]

    translations = {}
    while possible_translations:
        m = min(possible_translations, key=lambda x: len(x[1]))
        possible_translations.remove(m)
        for i in possible_translations:
            i[1].difference_update(m[1])

        translations[m[0]] = m[1].pop()

    m = 1
    for r in range(len(rules)):
        translation = translations[r]
        if rule_names[translation].startswith("departure"):
            m *= personal_ticket[r]

    print(m)


if __name__ == "__main__":
    main()
