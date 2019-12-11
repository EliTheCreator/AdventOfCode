import re

file = open("input", "r")
data = [[int(x) for x in re.findall("[0-9]+", line)] for line in file][0]


def parse(data):
    children, metas = data[:2]
    data = data[2:]
    scores = []
    totals = 0

    for _ in range(children):
        total, score, data = parse(data)
        totals += total
        scores.append(score)

    totals += sum(data[:metas])

    if children == 0:
        return (totals, sum(data[:metas]), data[metas:])
    else:
        return (
            totals,
            sum(scores[k - 1]
                for k in data[:metas] if k > 0 and k <= len(scores)),
            data[metas:]
        )


total, value, remaining = parse(data)

print('part 1:', total)
print('part 2:', value)
