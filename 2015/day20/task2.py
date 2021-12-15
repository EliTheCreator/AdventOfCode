import array


def main():
    with open("input", "r") as file:
        minPresents = int(file.readline())

    maxVal = minPresents // 20
    houses = array.array('L', [0 for _ in range(maxVal)])
    for i in range(1, maxVal):
        elveni = i * 11
        j = i
        for _ in range(50):
            if j >= maxVal:
                break
            houses[j] += elveni
            j += i

        if houses[i] >= minPresents:
            print(i)
            break


if __name__ == "__main__":
    main()
