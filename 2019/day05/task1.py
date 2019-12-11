import re

def main():
    file = open("input", "r")
    # file = open("day05//input", "r")
    a = [int(x) for x in re.findall("-?[0-9]+", file.readline())]
    file.close()

    i = 0
    while i<len(a):
        instr = a[i]
        op = instr % 100
        modeP1 = instr // 100% 10
        modeP2 = instr // 1000% 10
        modeP3 = instr // 10000 %10


        if op==1 or op==2:
            p1 = a[i+1] if modeP1 else a[a[i+1]] 
            p2 = a[i+2] if modeP2 else a[a[i+2]]
            result = p1 + p2 if op==1 else p1 * p2
            if modeP3:
                a[i+3] = result
            else:
                a[a[i+3]] = result
            i += 4
        elif op==3:
            inp = int(input())
            if modeP1:
                a[i+1] = inp
            else:
                a[a[i+1]] = inp
            i += 2
        elif op==4:
            outp = a[i+1] if modeP1 else a[a[i+1]]
            print(outp)
            i += 2
        elif op==5:
            p1 = a[i+1] if modeP1 else a[a[i+1]] 
            p2 = a[i+2] if modeP2 else a[a[i+2]]
            if p1:
                i = p2
            else:
                i += 3
        elif op==6:
            p1 = a[i+1] if modeP1 else a[a[i+1]]
            p2 = a[i+2] if modeP2 else a[a[i+2]]
            if p1:
                i += 3
            else:
                i = p2
        elif op==7:
            p1 = a[i+1] if modeP1 else a[a[i+1]] 
            p2 = a[i+2] if modeP2 else a[a[i+2]]
            result = 1 if p1 < p2 else 0
            if modeP3:
                a[i+3] = result
            else:
                a[a[i+3]] = result
            i += 4
        elif op==8:
            p1 = a[i+1] if modeP1 else a[a[i+1]] 
            p2 = a[i+2] if modeP2 else a[a[i+2]]
            result = 1 if p1 == p2 else 0
            if modeP3:
                a[i+3] = result
            else:
                a[a[i+3]] = result
            i += 4
        elif op==99:
            break
        else:
            print(f"Error: unknown Instruction")
            print(f"Instr:{str(instr).zfill(5)} Op:{op} P1:{modeP1} P2:{modeP2} P3:{modeP3}")
            return


main()