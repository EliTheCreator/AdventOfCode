import re


def main():
    file = open("input", "r")
    data = [int(x) for x in re.findall("[0-9]", file.readline())]
    file.close()

    size = 25 * 6
    image = [2 for _ in range(size)]

    for j in range(size):
        for i in range(0, len(data), size):
            val = data[i + j]
            if val != 2:
                image[j] = val
                break

    for j in range(6):
        startAt = j * 25
        print(
            "".join(["." if x == 0 else "#" for x in image[startAt:startAt+25]]))


main()
