from math import sqrt
import re


def main():
    with open("input", "r") as file:
        time, distance = [int("".join(re.findall(r"\d+", line))) for line in file.readlines()]

    intermediate = sqrt(time**2 - 4*distance)

    upper_bound = (time+intermediate)/2
    if int(upper_bound) == upper_bound:
        upper_bound -= 0.1
    lower_bound = (time-intermediate)/2

    product = int(upper_bound)-int(lower_bound)

    print(product)


if __name__ == "__main__":
    main()
