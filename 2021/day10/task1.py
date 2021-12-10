

def main():
    with open("input", "r") as file:
        data = [line.strip() for line in file.readlines()]

    values = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = 0
    for line in data:
        stack = []
        for bracket in line:
            if bracket in "([{<":
                stack.append(bracket)
            elif stack.pop() + bracket not in "()[]{}<>":
                score += values[bracket]
                break

    print(score)


if __name__ == "__main__":
    main()
