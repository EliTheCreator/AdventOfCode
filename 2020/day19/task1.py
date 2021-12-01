import re
from collections import defaultdict


def main():
    file = open("input", "r")
    raw_rules, raw_words = file.read().split("\n\n", maxsplit=1)
    file.close()
    raw_rules = raw_rules.split("\n")
    words = [word.strip() for word in raw_words.split("\n")]

    rules = defaultdict(lambda: set())
    terminal_rules = defaultdict(lambda: set())
    for raw_rule in raw_rules:
        left_side, right_sides = raw_rule.split(": ", maxsplit=1)
        number = int(left_side)

        for right_side in right_sides.split(" | "):
            nonterminals = [int(x) for x in re.findall(r"\d+", right_side)]
            if nonterminals:
                rules[number].add(tuple(nonterminals))
            else:
                terminal = re.findall(r"\w", right_side)[0]
                rules[number].add(terminal)
                terminal_rules[terminal].add(number)

    r = len(raw_rules)
    matches = 0
    for word in words:
        n = len(word)
        cyka = [[[False for _ in range(r)]
                 for _ in range(n)] for _ in range(n)]

        for i, c in enumerate(word):
            for v in terminal_rules[c]:
                cyka[0][i][v] = True

        print(word)
        for l in range(1, n):
            for s in range(n-l+1):
                for p in range(l-1):
                    for a, right_sides in rules.items():
                        for x in right_sides:
                            if len(x) > 1:
                                b, c = x
                                if cyka[p][s][b] and cyka[l-p][s+p][c]:
                                    cyka[l][s][a] = True

        if cyka[n-1][0][0]:
            matches += 1

    print(matches)


if __name__ == "__main__":
    main()
