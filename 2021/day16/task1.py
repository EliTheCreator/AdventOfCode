from functools import reduce


def main():
    with open("input", "r") as file:
        data = "".join([bin(int(char, 16))[2:].zfill(4)
                       for char in file.readline().strip()])

    def parse(data):
        pos = 0
        version = int(data[pos:pos+3], 2)
        typeId = int(data[pos+3:pos+6], 2)

        versionsSum = version

        pos += 6

        if typeId == 4:
            while data[pos] == "1":
                pos += 5
            pos += 5
        else:
            lengthTypeId = data[pos]
            pos += 1
            if lengthTypeId == "0":
                totalLength = int(data[pos:pos+15], 2)
                pos += 15
                end = pos + totalLength
                while pos < end:
                    lenSubPacket, versionSumSubPacket = parse(data[pos:])
                    pos += lenSubPacket
                    versionsSum += versionSumSubPacket
            else:
                numOfSubPackets = int(data[pos:pos+11], 2)
                pos += 11
                for _ in range(numOfSubPackets):
                    lenSubPacket, versionSumSubPacket = parse(data[pos:])
                    pos += lenSubPacket
                    versionsSum += versionSumSubPacket

        return pos, versionsSum

    print(parse(data)[1])


if __name__ == "__main__":
    main()
