import re


def main():
    file = open("input", "r")
    initialState = re.findall("[#.]+", file.readline())[0]
    state = set(index for index, letter in enumerate(
        initialState) if letter == '#')

    rules = set([pattern for pattern, rep in [re.findall("[#.]+", line)
                                              for line in file if line != "\n"] if rep == '#'])
    file.close()

    for _ in range(20):
        nextState = set()
        start = min(state) - 2
        end = max(state) + 3

        for i in range(start, end):
            pattern = "".join(
                ['#' if i + x in state else '.' for x in range(-2, 3)])
            if pattern in rules:
                nextState.add(i)

        state = nextState

    print(sum(state))


main()
