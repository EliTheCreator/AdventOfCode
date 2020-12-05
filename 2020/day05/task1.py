import os
import re


def main():
    file = open("input", "r")
    assignments = [x.strip() for x in file.readlines()]
    file.close()

    def calcSeat(assignment):
        def binarySearch(takeLower, takeUpper, minV, maxV, values):
            lower = minV
            upper = maxV
            for c in values:
                if c == takeLower:
                    upper = lower + ((upper - lower) // 2)
                else:
                    lower = lower + ((upper - lower + 1) // 2)
            return lower

        row = binarySearch('F', 'B', 0, 127, assignment[:7])
        column = binarySearch('L', 'R', 0, 7, assignment[7:])
        return row*8 + column

    print(max(map((lambda assignment: calcSeat(assignment)), assignments)))


if __name__ == "__main__":
    main()
