import re


def main():
    file = open("input", "r")
    subject_number, loop_size = [int(x)
                                 for x in re.findall(r"\d+", file.read())]
    file.close()

    value = 1
    for i in range(loop_size):
        value = (value * subject_number) % 20201227


if __name__ == "__main__":
    main()
