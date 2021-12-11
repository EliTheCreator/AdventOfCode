
def main():
    with open("input", "r") as file:
        password = [ord(c) - ord('a') for c in file.readline().strip()]

    illegalLetters = (ord('i') - ord('a'),
                      ord('o') - ord('a'),
                      ord('l') - ord('a'))

    while True:
        for i in range(len(password)-1, -1, -1):
            password[i] += 1
            if password[i]//26:
                password[i] %= 26
            else:
                break

        for letter in illegalLetters:
            if letter in password:
                break
        else:
            for i in range(len(password) - 2):
                a, b, c = password[i:i+3]
                if a + 2 == c and b + 1 == c:
                    break
            else:
                continue

            pairs = 0
            count = 1
            for i in range(len(password) - 1):
                if password[i] == password[i + 1]:
                    count += 1
                else:
                    if count == 2:
                        pairs += 1
                    count = 1

            if count == 2:
                pairs += 1
            if pairs >= 2:
                break

    print("".join([chr(c + ord('a')) for c in password]))


if __name__ == "__main__":
    main()
