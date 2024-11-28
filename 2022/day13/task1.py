from enum import Enum


class Result(Enum):
    UNDETERMINED = 0,
    INCORRECT_ORDER = 1,
    CORRECT_ORDER = 2


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
        pairs = [[eval(list) for list in line.split("\n")] for line in file.read().split("\n\n")]

    correctOrders = []
    for index, (left, right) in enumerate(pairs, start=1):
        result: Result = compare(left, right)
        # print(f"{index}:\t {result.name}")
        match result:
            case Result.CORRECT_ORDER:
                correctOrders.append(index)
            case _:
                pass

    print(sum(correctOrders))


if __name__ == "__main__":
    main()
