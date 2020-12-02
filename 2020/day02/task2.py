import os
import re


def main():
    file = open("input", "r")
    lines = [([int(x) for x in re.findall("[0-9]+", line)],
              [x for x in re.findall("[a-z]+", line)]) for line in file.readlines()]
    file.close()

    pw_counter = 0
    for (pos1, pos2), (ltr, pw) in lines:
        if (ltr == pw[pos1-1]) ^ (ltr == pw[pos2-1]):
            pw_counter += 1

    print(pw_counter)


if __name__ == "__main__":
    main()
