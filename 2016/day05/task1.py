from hashlib import md5
from itertools import count


def main():
    with open("input", "r") as file:
        doorId = file.readline().strip()

    password = []
    for index in count(1):
        doorAndIndex = doorId + str(index)
        hashed = md5(doorAndIndex.encode()).hexdigest()
        if hashed.startswith("00000"):
            password.append(hashed[5])
            if len(password) >= 8:
                break

    print("".join(password))


if __name__ == "__main__":
    main()
