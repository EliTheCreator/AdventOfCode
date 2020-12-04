import os
from hashlib import md5


def main():
    file = open("input", "r")
    seed = file.readline().strip()
    file.close()

    counter = 1
    while True:
        if md5(seed + str(counter)).hexdigest().startswith(6*"0"):
            print(counter)
            break
        counter += 1


if __name__ == "__main__":
    main()
