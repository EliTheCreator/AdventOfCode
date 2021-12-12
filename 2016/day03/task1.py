

def main():
    with open("input", "r") as file:
        triangles = [[int(x) for x in line.strip().split()]
                     for line in file.readlines()]

    possibleTriangles = 0
    for a, b, c in triangles:
        if a + b > c and a + c > b and b + c > a:
            possibleTriangles += 1

    print(possibleTriangles)


if __name__ == "__main__":
    main()
