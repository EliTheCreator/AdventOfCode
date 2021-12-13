import re
from string import ascii_uppercase


def main():
    with open("input", "r") as file:
        data = [line.strip() for line in file.readlines()]

    decompressedLength = 0
    for line in data:
        decompressedLine = ""
        i = 0
        oldLength = len(line)
        while i < oldLength:
            c = line[i]
            if c in ascii_uppercase:
                decompressedLine += c
                i += 1
            elif c == "(":
                i += 1
                sMarker = i
                while line[i] != ")":
                    i += 1
                eMarker = i
                i += 1
                cs, rs = (int(x)
                          for x in re.findall(r"\d+", line[sMarker:eMarker]))
                sData = i
                eData = min(i + cs, oldLength)
                for _ in range(rs):
                    for di in range(sData, eData):
                        decompressedLine += line[di]
                i = eData

        decompressedLength += len(decompressedLine)

    print(decompressedLength)


if __name__ == "__main__":
    main()
