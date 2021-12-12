from itertools import permutations


def main():
    with open("input", "r") as file:
        data = [(parts[0], int(parts[3]) if parts[2] == "gain" else -int(parts[3]), parts[-1])
                for parts in [line.strip()[:-1].split(" ") for line in file.readlines()]]

    weights = {}
    people = set()

    for alice, weight, bob in data:
        people.add(alice)
        people.add(bob)
        weights[(alice, bob)] = weight

    start, *others = people

    maxHappiness = 0
    for perm in permutations(others):
        curHappiness = 0
        cur = start
        for next in perm:
            curHappiness += weights[(cur, next)]
            curHappiness += weights[(next, cur)]
            cur = next
        curHappiness += weights[(cur, start)]
        curHappiness += weights[(start, cur)]

        maxHappiness = max(curHappiness, maxHappiness)

    print(maxHappiness)


if __name__ == "__main__":
    main()
