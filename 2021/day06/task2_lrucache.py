from functools import lru_cache
import re


@lru_cache(maxsize=266)
def fam_size(day):
    if day < 1:
        return 0
    elif day == 1:
        return 1
    else:
        return 1 + sum((fam_size(m) for m in range(day-9, 0, -7)))


def main():
    with open("input", "r") as file:
        lanternfish = [int(fish_age)
                       for fish_age in re.findall("[0-9]+", file.read())]

    last_day = 256
    print(sum([fam_size(last_day + (9 - fish_age))
          for fish_age in lanternfish]))


if __name__ == "__main__":
    main()
