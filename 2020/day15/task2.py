import re


def main():
    file = open("input", "r")
    data = [int(x) for x in re.findall(r"\d+", file.readline())]
    file.close()

    turns = {}
    for i, n in enumerate(data, start=1):
        turns[n] = i

    lastSpoken = data[-1]
    for turn in range(len(data), 30000000):
        dif = turn - turns[lastSpoken]
        turns[lastSpoken] = turn
        lastSpoken = dif
        turn += 1
        if lastSpoken not in turns:
            turns[lastSpoken] = turn

    print(lastSpoken)


if __name__ == "__main__":
    main()
