import os
import string


def main():
    file = open("input", "r")
    liste = [c for c in file.readline()][:-1]
    file.close()

    minimum = len(liste)

    for letter in string.ascii_lowercase:
        l2 = liste.copy()
        j = 0
        while j < len(l2):
            cur = l2[j]
            if cur.lower() == letter:
                l2.pop(j)
            else:
                j += 1

        i = 1
        while i < len(l2):
            prev = l2[i-1]
            cur = l2[i]

            if cur == prev.swapcase():
                l2.pop(i-1)
                l2.pop(i-1)
                if i > 1:
                    i -= 1
            else:
                i += 1

        if (len(l2) < minimum):
            minimum = len(l2)

    print(minimum)


main()
