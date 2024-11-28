import re


def main():
    with open("input", "r") as file:
        data = [[int(x) for x in re.findall(r"\d+", line)] for line in file.readlines()]

    matches_dp = [1 for _ in range(len(data))]
    for start_index, line in enumerate(data):
        matches = len(set.intersection(set(line[1:11]), set(line[11:])))
        for index in range(start_index+1, min(start_index+1+matches, len(matches_dp))):
            matches_dp[index] += matches_dp[start_index]

    print(sum(matches_dp))


if __name__ == "__main__":
    main()
