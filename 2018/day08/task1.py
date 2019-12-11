import re


def recr(data: [int]):
    s = 0
    c = data.pop(0)
    d = data.pop(0)

    for _ in range(c):
        s += recr(data)

    for _ in range(d):
        s += data.pop(0)

    return s


def main():
    file = open("input", "r")
    data = [[int(x) for x in re.findall("[0-9]+", line)] for line in file][0]
    file.close()

    print(recr(data))


main()
