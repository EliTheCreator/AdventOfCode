import os


def main():
    file = open("input", "r")
    liste = [c for c in file.readline()]
    file.close()

    i = 1
    while i < len(liste):
        prev = liste[i-1]
        cur = liste[i]

        if cur == prev.swapcase():
            liste.pop(i-1)
            liste.pop(i-1)
            if i > 1:
                i -= 1
        else:
            i += 1

    print(len(liste) - 1)


main()
