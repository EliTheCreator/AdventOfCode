import os
import re


def main():
    file = open("input", "r")
    assignments = [x.strip() for x in file.readlines()]
    file.close()

    maxRow = 127
    maxColumn = 7

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

        row = binarySearch('F', 'B', 0, maxRow, assignment[:7])
        column = binarySearch('L', 'R', 0, maxColumn, assignment[7:])
        return row*8 + column

    occupiedSeats = sorted(
        map((lambda assignment: calcSeat(assignment)), assignments))
    for seat in range(1, len(occupiedSeats)-1):
        if occupiedSeats[seat] + 2 == occupiedSeats[seat+1]:
            print(occupiedSeats[seat]+1)
            break

    # maxSeat = maxRow*8 + maxColumn
    # occupiedSeats = [False for _ in range(maxSeat)]
    # for assignment in assignments:
    #     occupiedSeats[calcSeat(assignment)] = True

    # for seat in range(1, maxSeat-1):
    #     if occupiedSeats[seat-1] and not occupiedSeats[seat] and occupiedSeats[seat+1]:
    #         print(seat)
    #         break


if __name__ == "__main__":
    main()
