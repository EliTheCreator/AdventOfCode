import re


def main():
    with open("input", "r") as file:
        data = [tuple([line.split(" ")[0]] + [int(x) for x in re.findall("\d+", line)])
                for line in file.readlines()]

    duration = 2503
    distances = []
    for _, speed, workTime, restingTime in data:
        fullRuns = duration // (workTime + restingTime)
        distance = speed * workTime * fullRuns
        leftover = duration % (workTime + restingTime)
        if leftover >= workTime:
            distance += speed * workTime
        else:
            distance += speed * leftover

        distances.append(distance)

    print(max(distances))


if __name__ == "__main__":
    main()
