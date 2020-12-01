import os
import re


def main():
    file = open("input", "r")
    ep = sorted([int(x) for x in file.readlines()])
    file.close()

    l = len(ep)
    for i in range(l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                vi, vj, vk = ep[i], ep[j], ep[k]
                v = vi + vj + vk
                if v == 2020:
                    print(vi * vj * vk)
                    return
                elif v > 2020:
                    break


if __name__ == "__main__":
    main()
