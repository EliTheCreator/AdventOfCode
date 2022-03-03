from re import findall


def main():

    with open("input", "r") as file:
        molecule = findall(r"[A-Z][a-z]?", file.read().split("\n\n")[1])

    rns = sum((1 for atom in molecule if atom == "Rn"))
    ys = sum((1 for atom in molecule if atom == "Y"))
    ars = sum((1 for atom in molecule if atom == "Ar"))
    print(len(molecule) - rns - 2*ys - ars - 1)


if __name__ == "__main__":
    main()
