import os
import re


def main():
    file = open("input", "r")
    lines = [([int(x) for x in re.findall("[0-9]+", line)],
              [x for x in re.findall("[a-z]+", line)]) for line in file.readlines()]
    file.close()

    pw_counter = 0
    for (lower, upper), (ltr, pw) in lines:
        ltr_counter = 0
        for l in pw:
            if l == ltr:
                ltr_counter += 1

        if lower <= ltr_counter & ltr_counter <= upper:
            pw_counter += 1

    print(pw_counter)


if __name__ == "__main__":
    main()
