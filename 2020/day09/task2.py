import os
import re


def main():
    file = open("input", "r")
    data = [int(x) for x in file.readlines()]
    file.close()

    specialNum = 0
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
            specialNum = num
            break

        summands.remove(data[i-25])
        summands.append(num)
        summands.sort()

    left = 0
    right = 1
    localSum = data[0] + data[1]
    while localSum != specialNum:
        if localSum < specialNum:
            right += 1
            localSum += data[right]
        else:
            localSum -= data[left]
            left += 1

    print(min(data[left:right+1]) + max(data[left:right+1]))


if __name__ == "__main__":
    main()
