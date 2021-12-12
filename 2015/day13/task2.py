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

    me = "Elias"
    for person in people:
        for perm in permutations([me, person]):
            weights[perm] = 0

    people.add(me)

    start, *others = people

    maxHappiness = 0
    for perm in permutations(others):
        curHappiness = 0
        cur = start
        for next in perm:
            for perm2 in permutations([cur, next]):
                curHappiness += weights[perm2]
            cur = next

        for perm2 in permutations([cur, start]):
            curHappiness += weights[perm2]

        maxHappiness = max(curHappiness, maxHappiness)

    print(maxHappiness)


if __name__ == "__main__":
    main()
