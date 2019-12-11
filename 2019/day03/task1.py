import re

def main():
    file = open("input", "r")
    cablea = [(x[0], int(x[1:])) for x in re.findall("[[A-Z][0-9]+", file.readline())]
    cableb = [(x[0], int(x[1:])) for x in re.findall("[[A-Z][0-9]+", file.readline())]
    file.close()

    horizontalsa = []
    verticalsa = []
    horizontalsb = []
    verticalsb = []

    minDist = 9999999999

    cx = 0
    cy = 0
    for direct, dist in cablea:
        if direct == "R":
            horizontalsa.append(((cx , cy), (cx + dist, cy)))
            cx += dist
        elif direct == "L":
            horizontalsa.append(((cx - dist, cy), (cx, cy)))
            cx -= dist
        elif direct == "U":
            verticalsa.append(((cx, cy), (cx, cy + dist)))
            cy += dist
        elif direct == "D":
            verticalsa.append(((cx, cy - dist), (cx, cy)))
            cy -= dist
        else:
            print(f"Error: no direction {direct}")

    cx = 0
    cy = 0
    for direct, dist in cableb:
        if direct == "R":
            horizontalsb.append(((cx , cy), (cx + dist, cy)))
            cx += dist
        elif direct == "L":
            horizontalsb.append(((cx - dist, cy), (cx, cy)))
            cx -= dist
        elif direct == "U":
            verticalsb.append(((cx, cy), (cx, cy + dist)))
            cy += dist
        elif direct == "D":
            verticalsb.append(((cx, cy - dist), (cx, cy)))
            cy -= dist
        else:
            print(f"Error: no direction {direct}")


    minDist = 9999999999

    for (hx1, hy1), (hx2, _) in horizontalsa:
        for (vx1, vy1), (_, vy2) in verticalsb:
            if (hx1 < vx1 and vx1 < hx2) and (vy1 < hy1 and hy1 < vy2):
                manDist = abs(hy1) + abs(vx1)
                if manDist < minDist:
                    minDist = manDist

    for (hx1, hy1), (hx2, _) in horizontalsb:
        for (vx1, vy1), (_, vy2) in verticalsa:
            if (hx1 < vx1 and vx1 < hx2) and (vy1 < hy1 and hy1 < vy2):
                manDist = abs(hy1) + abs(vx1)
                if manDist < minDist:
                    minDist = manDist

    print(minDist)


main()