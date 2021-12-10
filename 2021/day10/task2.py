

def main():
    with open("input", "r") as file:
        data = [line.strip() for line in file.readlines()]

    values = {"(": 1, "[": 2, "{": 3, "<": 4}
    scores = []
    for line in data:
        stack = []
        for bracket in line:
            if bracket in "([{<":
                stack.append(bracket)
            elif stack.pop() + bracket not in "()[]{}<>":
                break
        else:
            score = 0
            while stack:
                score = score * 5 + values[stack.pop()]

            scores.append(score)

    scores.sort()
    print(scores[len(scores) // 2])


if __name__ == "__main__":
    main()
