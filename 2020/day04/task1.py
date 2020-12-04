import os
import re


def main():
    file = open("input", "r")
    passports = [[field.split(":")[0] for field in re.findall(
        "[a-z]+:[#a-z0-9]+", line)] for line in file.read().split("\n\n")]
    file.close()

    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    valids = len(list(filter(
        None, map((lambda p: all(map((lambda r: r in p), required))), passports))))

    # valids = 0
    # for passport in raw_passports:
    #     if all(map((lambda r: r in passport), required)):
    #         valids += 1

    print(valids)


if __name__ == "__main__":
    main()
