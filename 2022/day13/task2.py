from enum import Enum
from functools import cmp_to_key


class Result(int, Enum):
    CORRECT_ORDER = -1,
    UNDETERMINED = 0,
    INCORRECT_ORDER = 1,


def compare(left, right) -> Result:
    result: Result = Result.UNDETERMINED
    match (isinstance(left, list), isinstance(right, list)):
        case (True, True):
            for pair in zip(left, right):
                result = compare(*pair)
                if result != Result.UNDETERMINED:
                    break

            if result == Result.UNDETERMINED:
                if len(left) < len(right):
                    result = Result.CORRECT_ORDER
                elif len(left) > len(right):
                    result = Result.INCORRECT_ORDER
                else:
                    result = Result.UNDETERMINED
        case (False, False):
            if left < right:
                result = Result.CORRECT_ORDER
            elif left > right:
                result = Result.INCORRECT_ORDER
            else:
                result = Result.UNDETERMINED
        case (True, False):
            result = compare(left, [right])
        case (False, True):
            result = compare([left], right)

    return result


def main():
    with open("input", "r") as file:
        lists = [eval(list) for line in file.read().split("\n\n") for list in line.split("\n")]

    dividerOne = [[2]]
    dividerTwo = [[6]]
    lists.append(dividerOne)
    lists.append(dividerTwo)

    lists.sort(key=cmp_to_key(compare))
    firstIndex = lists.index(dividerOne) + 1
    secondIndex = lists.index(dividerTwo) + 1

    print(firstIndex * secondIndex)


if __name__ == "__main__":
    main()
