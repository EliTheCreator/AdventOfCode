import os
import re


def main():
    file = open("input", "r")
    passports = [[field.split(":") for field in re.findall(
        "[a-z]+:[#a-z0-9]+", line)] for line in file.read().split("\n\n")]
    file.close()

    # required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    def validate(field):
        key, value = field
        if key in ["byr", "iyr", "eyr"]:
            try:
                year = int(value)
            except:
                return False

            if key == "byr":
                if 1920 <= year <= 2002:
                    return True
                else:
                    return False
            elif key == "iyr":
                if 2010 <= year <= 2020:
                    return True
                else:
                    return False
            else:
                if 2020 <= year <= 2030:
                    return True
                else:
                    return False
        elif key == "hgt":
            try:
                size = int(value[:-2])
            except:
                return False
            unit = value[-2:]

            if unit == "cm" and 150 <= size <= 193:
                return True
            elif unit == "in" and 59 <= size <= 73:
                return True
            else:
                return False
        elif key == "hcl":
            return re.fullmatch("#[0-9a-f]{6}", value) != None
        elif key == "ecl":
            return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        elif key == "pid":
            if len(value) == 9:
                try:
                    int(value)
                except:
                    return False
                return True
        else:
            return False

    # valids = 0
    # for passport in passports:
    #     if all(map((lambda r: r in [x[0] for x in passport]), required)):
    #         if len(list(filter(None, map((lambda field: validate(field)), passport)))) == 7:
    #             valids += 1

    valids = len(list(filter((lambda x: x >= 7), map((lambda p: len(
        list(filter(None, map((lambda f: validate(f)), p))))), passports))))
    print(valids)


if __name__ == "__main__":
    main()
