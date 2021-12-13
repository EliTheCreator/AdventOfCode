import re
from string import ascii_uppercase


def decompress(lineSnippet):
    decompressedLength = 0
    i = 0
    oldLength = len(lineSnippet)
    while i < oldLength:
        c = lineSnippet[i]
        i += 1
        if c in ascii_uppercase:
            decompressedLength += 1
        elif c == '(':
            sMarker = i
            while lineSnippet[i] != ')':
                i += 1
            eMarker = i
            cs, rs = (int(x)
                      for x in re.findall(r"\d+", lineSnippet[sMarker:eMarker]))
            i += 1
            sData = i
            eData = min(i + cs, oldLength)
            decompressedLength += rs * \
                decompress(lineSnippet[sData: eData])
            i = eData

    return decompressedLength


def main():
    with open("input", "r") as file:
        data = [line.strip() for line in file.readlines()]

    decompressedLength = 0
    for line in data:
        decompressedLength += decompress(line)

    print(decompressedLength)


if __name__ == "__main__":
    main()
