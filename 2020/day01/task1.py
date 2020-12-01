import os
import re


def main():
    file = open("input", "r")
    ep = [int(x) for x in file.readlines()]
    file.close()

    for i in range(len(ep)):
        for j in range(i+1, len(ep)):
            if ep[i] + ep[j] == 2020:
                print(ep[i] * ep[j])


if __name__ == "__main__":
    main()
