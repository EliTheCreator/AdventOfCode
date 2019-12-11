import os
import difflib


def main():
    file = open("input", "r")
    lines = [line[:-1] for line in file]

    def first_list_gen(lines):
        for num, line in zip(range(0, len(lines)).__reversed__(), lines):
            for _ in range(num):
                yield(line)

    def second_list_gen(lines):
        for num in range(1, len(lines)):
            for line in lines[num:]:
                yield(line)

    for pair in zip(first_list_gen(lines), second_list_gen(lines)):
        s = difflib.SequenceMatcher(
            None, pair[0], pair[1]).get_matching_blocks()

        if (s[0][2] + s[1][2] == len(pair[0]) - 1):
            print(pair[0][s[0][0]:s[0][0]+s[0][2]] +
                  pair[0][s[1][0]:s[1][0]+s[1][2]])
            break

    file.close()


main()
