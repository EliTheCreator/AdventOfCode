import re

def main():
    file = open("input", "r")
    a = [int(x) for x in re.findall("[0-9]+", file.readline())]
    file.close()

    a[1] = 12
    a[2] = 2

    i = 0
    while i<len(a):
        op = a[i]

        if op==1:
            a[a[i+3]] = a[a[i+1]] + a[a[i+2]]
        elif op==2:
            a[a[i+3]] = a[a[i+1]] * a[a[i+2]]
        elif op==99:
            break
        else:
            print(f"Error: wrong opcode {a[i]}")
            return

        i += 4

    print(a[0])


main()