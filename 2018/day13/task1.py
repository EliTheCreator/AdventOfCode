
class trackPart:
    isIntersection: bool
    func = None

    def __init__(self, isIntersection: bool, func):
        self.isIntersection = isIntersection
        self.func = func

    def next(self, direction: int, state: int):
        return self.func(direction, state)


class cart:
    orientation: int
    position: tuple
    state: int
    tracks: dict
    track = None

    def __init__(self, tracks, orientation: int, position: tuple):
        self.orientation = orientation
        self.position = position
        self.state = 0
        self.tracks = tracks
        self.track = self.tracks[self.position]

    def incState(self):
        self.state = (self.state + 1) % 3

    def next(self):
        nextOrientation = self.track.next(self.orientation, self.state)
        if self.track.isIntersection:
            self.incState()

        x, y = self.position
        if nextOrientation == 0:
            self.position = (x, y - 1)
        elif nextOrientation == 1:
            self.position = (x + 1, y)
        elif nextOrientation == 2:
            self.position = (x, y + 1)
        elif nextOrientation == 3:
            self.position = (x - 1, y)

        self.track = self.tracks[self.position]
        self.orientation = nextOrientation

        return self.position


def main():
    file = open("input", "r")

    tracks = {}
    cartsCoords = []
    for y, line in enumerate(file):
        for x, char in enumerate(line[:-1]):
            isIntersection = False
            func = None

            if char == "/":
                func = lambda x, y: (3*x + 1) % 4
            elif char == "\\":
                func = lambda x, y: (3*x + 3) % 4
            elif char == "+":
                isIntersection = True
                func = lambda x, y: (x + (3,0,1)[y]) % 4
            elif char in ("|", "-", "^", ">", "v", "<"):
                func = lambda x, y: x
                if char in ("^", ">", "v", "<"):
                    orientation: int
                    if char == "^":
                        orientation = 0
                    elif char == ">":
                        orientation = 1
                    elif char == "v":
                        orientation = 2
                    elif char == "<":
                        orientation = 3

                    cartsCoords.append(((x, y), orientation))

            if func:
                tracks[(x, y)] = trackPart(isIntersection, func)

    file.close()

    carts = []
    occupiedTracks = set()
    for c in cartsCoords:
        occupiedTracks.add(c[0])
        carts.append(cart(tracks, c[1], c[0]))

    chrashFree = True
    while chrashFree:
        for c in carts:
            occupiedTracks.remove(c.position)
            coords = c.next()
            if coords in occupiedTracks:
                chrashFree = False
                print(f"{coords[0]},{coords[1]}")
                break
            else:
                occupiedTracks.add(coords)

        carts = sorted(carts, key=lambda x: [x.position[0], x.position[1]])


if __name__ == "__main__":
    main()
