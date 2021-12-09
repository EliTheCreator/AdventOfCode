import re


def main():
    with open("input", "r") as file:
        data = [([set(x) for x in re.findall("[a-g]+", line.split("|")[0])],
                 re.findall("[a-g]+", line.split("|")[1]))
                for line in file.readlines()]

    wires_to_digit = {
        "abcefg": "0",
        "cf": "1",
        "acdeg": "2",
        "acdfg": "3",
        "bcdf": "4",
        "abdfg": "5",
        "abdefg": "6",
        "acf": "7",
        "abcdefg": "8",
        "abcdfg": "9"
    }

    total_sum = 0
    for (digits, numbers) in data:
        cf = set()
        bcdf = set()
        acf = set()
        abcdefg = set()
        adg = set("abcdefg")
        abfg = set("abcdefg")

        for digit in digits:
            match (len(digit)):
                case 2:
                    cf = digit
                case 3:
                    acf = digit
                case 4:
                    bcdf = digit
                case 5:
                    adg &= digit
                case 6:
                    abfg &= digit
                case 7:
                    abcdefg = digit
                case _:
                    pass

        a = acf - cf
        b = bcdf - cf - adg
        c = cf - abfg
        d = adg - abfg - cf
        e = abcdefg - bcdf - adg
        f = cf - c
        g = adg - a - d

        translation = dict(((ord(k.pop()), v)
                            for (k, v)
                            in zip((a, b, c, d, e, f, g), "abcdefg")
                            ))

        numbers_translated = ["".join(sorted(number.translate(translation)))
                              for number in numbers]

        total_sum += int("".join([wires_to_digit[number]
                         for number in numbers_translated]))

    print(total_sum)


if __name__ == "__main__":
    main()
