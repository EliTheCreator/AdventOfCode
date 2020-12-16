import re


def main():
    file = open("input", "r")
    raw_rules, _, raw_tickets = file.read().split("\n\n")
    file.close()

    rules = [[int(x) for x in re.findall(r"\d+", line)]
             for line in raw_rules.splitlines()]
    nearby_tickets = [[int(x) for x in re.findall(r"\d+", line)]
                      for line in raw_tickets.splitlines()[1:]]

    invalid_sum = 0
    for ticket in nearby_tickets:
        for value in ticket:
            valid = False
            for r1l, r1h, r2l, r2h in rules:
                if r1l <= value <= r1h or r2l <= value <= r2h:
                    valid = True
                    break

            if not valid:
                invalid_sum += value

    print(invalid_sum)


if __name__ == "__main__":
    main()
