
def main():
    with open("input", "r") as file:
        stream = file.read().strip()

    markerLength = 14
    for end in range(markerLength, len(stream)+1):
        if len(set(stream[end-markerLength:end])) == markerLength:
            print(end)
            break


if __name__ == "__main__":
    main()
