import re

def main():
    file = open("input", "r")
    b = [int(x) for x in re.findall("[0-9]+", file.readline())]
    file.close()

    for noun in range(100):
        for verb in range(100):
            a = b.copy()
            a[1] = noun
            a[2] = verb

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
                    break

                i += 4

            if a[0] == 19690720:
                print(100*noun + verb)


main()