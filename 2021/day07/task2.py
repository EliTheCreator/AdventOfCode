import re


def main():
    with open("input", "r") as file:
        positons = [int(x) for x in re.findall("[0-9]+", file.read())]

    mean = int(sum(positons) / len(positons))
    def sum_to_n(n): return (n * (n + 1)) // 2
    d1 = sum((sum_to_n(abs(mean - pos)) for pos in positons))
    d2 = sum((sum_to_n(abs(mean + 1 - pos)) for pos in positons))
    print(min(d1, d2))


if __name__ == "__main__":
    main()
