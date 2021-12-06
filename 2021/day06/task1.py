import re


def main():
    with open("input", "r") as file:
        lanternfish = [int(fish_age)
                       for fish_age in re.findall("[0-9]+", file.read())]

    last_day = 80
    dptable = {}

    for day in range(1, last_day + 10):
        total = 1
        for child_fish_age in range(day-9, 0, -7):
            total += dptable[child_fish_age]

        dptable[day] = total

    print(sum([dptable[last_day + (9 - fish_age)]
          for fish_age in lanternfish]))


if __name__ == "__main__":
    main()
