from functools import reduce


def main():
    with open("input", "r") as file:
        data = "".join([bin(int(char, 16))[2:].zfill(4)
                       for char in file.readline().strip()])

    def parse(data):
        pos = 0
        typeId = int(data[pos+3:pos+6], 2)

        packetValue = 0

        pos += 6

        if typeId == 4:
            value = ""
            while data[pos] == "1":
                value += data[pos+1:pos+5]
                pos += 5
            value += data[pos+1:pos+5]
            packetValue = int(value, 2)
            pos += 5
        else:
            lengthTypeId = data[pos]
            pos += 1
            subPacketValues = []
            if lengthTypeId == "0":
                totalLength = int(data[pos:pos+15], 2)
                pos += 15
                end = pos + totalLength
                while pos < end:
                    lenSubPacket, valueSubPacket = parse(data[pos:])
                    pos += lenSubPacket
                    subPacketValues.append(valueSubPacket)
            else:
                numOfSubPackets = int(data[pos:pos+11], 2)
                pos += 11
                for _ in range(numOfSubPackets):
                    lenSubPacket, valueSubPacket = parse(data[pos:])
                    pos += lenSubPacket
                    subPacketValues.append(valueSubPacket)

            match typeId:
                case 0:
                    packetValue = sum(subPacketValues)
                case 1:
                    packetValue = reduce(
                        lambda a, b: a * b, subPacketValues)
                case 2:
                    packetValue = min(subPacketValues)
                case 3:
                    packetValue = max(subPacketValues)
                case 5:
                    packetValue = subPacketValues[0] > subPacketValues[1]
                case 6:
                    packetValue = subPacketValues[0] < subPacketValues[1]
                case 7:
                    packetValue = subPacketValues[0] == subPacketValues[1]
                case _:
                    pass

        return pos, packetValue

    print(parse(data)[1])


if __name__ == "__main__":
    main()
