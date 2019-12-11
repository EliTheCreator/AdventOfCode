import re


def main():
    file = open("input", "r")
    initialState = re.findall("[#.]+", file.readline())[0]
    state = set(index for index, letter in enumerate(
        initialState) if letter == '#')

    rules = set([pattern for pattern, rep in [re.findall("[#.]+", line)
                                              for line in file if line != "\n"] if rep == '#'])
    file.close()

    prevSum = sum(state)
    prevDiv = 0

    for j in range(500):
        nextState = set()
        start = min(state) - 2
        end = max(state) + 3

        for i in range(start, end):
            pattern = "".join(
                ['#' if i + x in state else '.' for x in range(-2, 3)])
            if pattern in rules:
                nextState.add(i)

        curSum = sum(nextState)
        # print(f"Step: {j}   Cur: {curSum}    diff: {curSum-prevSum}")
        prevDiv = curSum - prevSum
        prevSum = curSum
        state = nextState

    print((50000000000 - 500) * prevDiv + prevSum)


main()
