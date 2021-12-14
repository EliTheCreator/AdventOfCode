from collections import defaultdict
from hashlib import md5
from itertools import count
from re import search


def main():
    with open("input", "r") as file:
        salt = file.readline().strip()

    keys = []
    candidates = defaultdict(lambda: set())
    for index in count(1):
        hash = md5(f"{salt}{index}".encode()).hexdigest()

        if match5 := search(r"(.)\1{4}", hash):
            letter = hash[match5.start()]
            for candidate in sorted(candidates[letter]):
                if index - candidate <= 1000:
                    keys.append(candidate)
                    if len(keys) == 64:
                        print(sorted(keys)[-1])
                        return
            candidates[letter] = set()

        if match3 := search(r"(.)\1{2}", hash):
            letter = hash[match3.start()]

            candidates[letter].add(index)


if __name__ == "__main__":
    main()
