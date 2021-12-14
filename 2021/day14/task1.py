from collections import defaultdict, deque


def main():
    with open("input", "r") as file:
        template, transitionsRaw = file.read().split("\n\n")

    template = deque(template)
    transitions = dict((line.strip().split(" -> ")
                        for line in transitionsRaw.split("\n")))

    for _ in range(10):
        for _ in range(len(template) - 1):
            pair = template[0] + template[1]
            if pair in transitions:
                template.rotate(-1)
                template.insert(0, transitions[pair])

            template.rotate(-1)
        template.rotate(-1)

    count = defaultdict(lambda: 0)
    for letter in template:
        count[letter] += 1

    print(max(count.values()) - min(count.values()))


if __name__ == "__main__":
    main()
