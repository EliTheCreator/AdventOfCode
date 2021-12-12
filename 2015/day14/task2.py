import re


def main():
    with open("input", "r") as file:
        data = [tuple([line.split(" ")[0]] + [int(x) for x in re.findall("\d+", line)])
                for line in file.readlines()]

    duration = 2503
    reindeerNames = set([reindeer[0] for reindeer in data])
    leaderboard = dict([(reindeer, 0) for reindeer in reindeerNames])
    for round in range(1, duration + 1):
        distances = []
        for reindeer, speed, workTime, restingTime in data:
            fullRuns = round // (workTime + restingTime)
            distance = speed * workTime * fullRuns
            leftover = round % (workTime + restingTime)
            if leftover >= workTime:
                distance += speed * workTime
            else:
                distance += speed * leftover

            distances.append((reindeer, distance))

        _, maxDistance = max(distances, key=lambda x: x[1])
        for name, distance in distances:
            if distance == maxDistance:
                leaderboard[name] += 1

    print(max(leaderboard.values()))


if __name__ == "__main__":
    main()
