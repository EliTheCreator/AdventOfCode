import os
import re


def main():
    file = open("input", "r")
    data = [int(x) for x in file.readlines()]
    file.close()

    summands = sorted(data[:25])
    for i, num in enumerate(data[25:], 25):
        sumExists = False
        left = 0
        right = 24
        while left < right:
            localSum = summands[left] + summands[right]
            if num > localSum:
                left += 1
            elif num < localSum:
                right -= 1
            else:
                sumExists = True
                break

        if not sumExists:
            print(num)
            break

        summands.remove(data[i-25])
        summands.append(num)
        summands.sort()


if __name__ == "__main__":
    main()
