import os


def main():

    frequencies = set()
    sum = 0
    frequencies.add(sum)

    while True:
        file = open("input", "r")
        for line in file:
            sum += int(line)
            if frequencies.__contains__(sum):
                print(sum)
                file.close()
                return
            else:
                frequencies.add(sum)
        file.close()


main()
