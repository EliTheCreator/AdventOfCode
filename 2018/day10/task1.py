import re

def main():
    file = open("input", "r")
    data = [[int(x) for x in re.findall("-?[0-9]+", line)] for line in file]
    file.close()


    for i in range(10500):
        for line in data:
            line[0] += line[2]
            line[1] += line[3]

        if 10450 <= i and i <= 10470:
            minX = min(data, key=lambda x: x[0])[0]
            maxX = max(data, key=lambda x: x[0])[0]
            minY = min(data, key=lambda x: x[1])[1]
            maxY = max(data, key=lambda x: x[1])[1]
            
            sizeX = abs(maxX-minX)
            sizeY = abs(maxY-minY)
            graph = [["." for _ in range(sizeX+1)] for _ in range(sizeY+1)]
            for x, y, *_ in data:
                graph[y-minY][x-minX]= "#"
            print(i+1)
            for line in graph:
                print("".join(line))
            input()
    

main()