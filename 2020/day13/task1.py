import re


def main():
    file = open("input", "r")
    earliest = int(file.readline().strip())
    buses = [int(x) for x in re.findall(r"\d+", file.readline())]
    file.close()

    times = [earliest // bestBus
             if earliest % bestBus == 0
             else earliest // bestBus + 1
             for bestBus in buses]

    waitTime = max(buses)
    bestBus = 0
    for time, bus in zip(times, buses):
        dif = (time * bus) - earliest
        if dif < waitTime:
            waitTime = dif
            bestBus = bus

    print(bestBus*waitTime)


if __name__ == "__main__":
    main()
