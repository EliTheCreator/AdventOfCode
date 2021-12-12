

def main():
    with open("input", "r") as file:
        triangles = [[int(x) for x in line.strip().split()]
                     for line in file.readlines()]

    possibleTriangles = 0
    for col in range(len(triangles[0])):
        for row in range(0, len(triangles), 3):
            a = triangles[row][col]
            b = triangles[row + 1][col]
            c = triangles[row + 2][col]
            if a + b > c and a + c > b and b + c > a:
                possibleTriangles += 1

    print(possibleTriangles)


if __name__ == "__main__":
    main()
