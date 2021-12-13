from hashlib import md5
from itertools import count


def main():
    with open("input", "r") as file:
        doorId = file.readline().strip()

    password = {}
    for index in count(1):
        doorAndIndex = doorId + str(index)
        hashed = md5(doorAndIndex.encode()).hexdigest()
        if hashed.startswith("00000"):
            if hashed[5] in "01234567" and hashed[5] not in password:
                password[hashed[5]] = hashed[6]
                if len(password) >= 8:
                    break

    print("".join([c for _, c in sorted(password.items(), key=lambda k: k[0])]))


if __name__ == "__main__":
    main()
