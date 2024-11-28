
def main():
    with open("input", "r") as file:
        stream = file.read().strip()

    marker_length = 4
    for end in range(marker_length, len(stream)+1):
        if len(set(stream[end-marker_length:end])) == marker_length:
            print(end)
            break


if __name__ == "__main__":
    main()
